import logging
import json
import traceback
import multiprocessing
import os
import mimetypes
from pathlib import Path
import hashlib
import sqlite3
import bibtexparser
import pymupdf4llm
from dataclasses import dataclass
from typing import Dict, List
from tqdm.contrib.concurrent import process_map

logger = logging.getLogger(__name__)

@dataclass
class ProcessingResult:
    """Result of processing a bibliography entry.
    
    Attributes:
        citation_key: The citation key from the bibliography entry
        file_hashes: Dictionary mapping file paths to their SHA-256 hashes
        dir_hash: Hash of the directory contents (excluding linked file contents)
        success: Whether the processing was successful
    """
    citation_key: str
    file_hashes: Dict[str, str]
    dir_hash: str
    success: bool

def standalone_process_entry(args):
    """Process a single bibliography entry in a separate process.
    
    Args:
        args: Tuple of (entry, output_dir)
            entry: Dictionary containing the bibliography entry data
            output_dir: Path to the output directory
            
    Returns:
        ProcessingResult: Object containing processing results and status
    """
    entry, output_dir = args
    try:
        citation_key = entry.get('ID')
        if not citation_key:
            logger.warning("Entry missing citation key, skipping")
            return ProcessingResult(citation_key="", file_hashes={}, dir_hash="", success=False)
        
        entry_dir = output_dir / citation_key
        entry_dir.mkdir(exist_ok=True, parents=True)
        processed_contents = []
        current_hashes = {}
        
        # Parse and validate files
        file_field = entry.get('file', '')
        logger.debug(f"File field for {citation_key}: {file_field}")
        
        # Helper functions needed by standalone_process_entry
        def parse_file_field(file_field: str) -> List[Path]:
            if not file_field:
                return []
            
            paths = []
            for f in file_field.split(';'):
                try:
                    if ':' in f:
                        # Handle Zotero-style file fields (description:filepath)
                        _, file_path = f.split(':', 1)
                    else:
                        file_path = f
                        
                    file_path = file_path.strip()
                    if not file_path:
                        continue
                        
                    path = Path(file_path)
                    if path.exists():
                        logger.debug(f"Found file at: {path}")
                        paths.append(path)
                    else:
                        logger.warning(f"Could not find file: {file_path} for citation key: {citation_key}")
                except Exception as e:
                    logger.error(f"Failed to parse file field entry '{f}': {e}\n{traceback.format_exc()}")
            
            return paths

        def compute_file_hash(filepath: str) -> str:
            try:
                with open(filepath, 'rb') as f:
                    return hashlib.sha256(f.read()).hexdigest()
            except Exception as e:
                logger.error(f"Failed to compute hash for {filepath}: {e}\n{traceback.format_exc()}")
                return ""

        def compute_dir_hash(directory: Path) -> str:
            if not directory.exists():
                return ""
            
            # Get all files in directory, including symlinks
            files = sorted(f for f in directory.glob('**/*') if f.is_file() or f.is_symlink())
            hasher = hashlib.sha256()
            
            for file_path in files:
                try:
                    # Add relative path to hash
                    rel_path = file_path.relative_to(directory)
                    hasher.update(str(rel_path).encode())
                    
                    if file_path.is_symlink():
                        # For symlinks, hash only the target path string
                        target_path = os.readlink(file_path)
                        hasher.update(str(target_path).encode())
                    else:
                        # For regular files, hash the contents
                        with open(file_path, 'rb') as f:
                            for chunk in iter(lambda: f.read(4096), b''):
                                hasher.update(chunk)
                except Exception as e:
                    logger.error(f"Failed to hash file {file_path}: {e}\n{traceback.format_exc()}")
                    
            return hasher.hexdigest()
        
        file_paths = parse_file_field(file_field)
        
        if not file_paths:
            logger.warning(f"No files found for entry {citation_key}")
            return ProcessingResult(citation_key=citation_key, file_hashes={}, dir_hash="", success=False)
        
        # Create symbolic links to original files
        for file_path in file_paths:
            link_path = entry_dir / file_path.name
            if link_path.exists() or link_path.is_symlink():
                link_path.unlink()
            link_path.symlink_to(file_path.resolve())
            logger.debug(f"Created symbolic link: {link_path} -> {file_path}")
        
        # Process files
        for file_path in file_paths:
            mime_type, _ = mimetypes.guess_type(file_path)
            
            if mime_type == 'application/pdf':
                # Process PDF to markdown with images, using absolute paths
                md_text = pymupdf4llm.to_markdown(
                    str(file_path.resolve()),
                    write_images=True,
                    image_path=str(entry_dir),
                    show_progress=False  # Disable pymupdf4llm progress bar
                )
                processed_contents.append(md_text)
                logger.info(f"Successfully processed PDF {file_path}")
            
            elif mime_type and mime_type.startswith('text/'):
                # Process text files by wrapping in markdown code blocks
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                file_type = file_path.suffix.lstrip('.')
                md_text = f"```{file_type}\n{content}\n```"
                processed_contents.append(md_text)
                logger.info(f"Successfully processed text file {file_path}")
            else:
                logger.warning(f"Unsupported file type for {file_path}")
        
        if processed_contents:
            # Write combined markdown content with citation key header
            final_content = f"# Citation Key: {citation_key}\n\n---\n\n" + '\n\n---\n\n'.join(processed_contents)
            final_md = entry_dir / f"{citation_key}.md"
            final_md.write_text(final_content)
            
            # Compute hashes for change tracking
            current_hashes = {
                str(path): compute_file_hash(str(path))
                for path in file_paths
            }
        
        # Compute directory hash after all processing is done
        new_dir_hash = compute_dir_hash(entry_dir)
        logger.info(f"Successfully processed entry {citation_key}")
        return ProcessingResult(
            citation_key=citation_key,
            file_hashes=current_hashes,
            dir_hash=new_dir_hash,
            success=True
        )
    except Exception as e:
        logger.error(f"Failed to process entry {citation_key}: {e}\n{traceback.format_exc()}")
        return ProcessingResult(citation_key=citation_key, file_hashes={}, dir_hash="", success=False)

class BibliographyProcessor:
    def __init__(self, bib_file: str, dry_run: bool = False, quiet: bool = False):
        """Initialize the bibliography processor.
        
        Args:
            bib_file: Path to the bibliography file to process
            dry_run: If True, show what would be processed without actually doing it
            quiet: If True, suppress all output except warnings and errors
            
        The processor will create an output directory named '{bib_file_stem}-bib4llm'
        and initialize a SQLite database to track processed files.
        """
        self.bib_file = Path(bib_file).resolve()
        if not self.bib_file.exists():
            raise FileNotFoundError(f"BibTeX file not found: {self.bib_file}")
            
        self.dry_run = dry_run
        self.quiet = quiet
        self.output_dir = (Path.cwd() / f"{self.bib_file.stem}-bib4llm").resolve()
        
        if not self.dry_run:
            self.output_dir.mkdir(exist_ok=True)
            
            # Initialize database
            self.db_path = self.output_dir / "processed_files.db"
            
            # Initialize database schema
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS processed_items (
                        citation_key TEXT PRIMARY KEY,
                        file_hashes TEXT,
                        last_processed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        dir_hash TEXT
                    )
                """)
                conn.commit()
        
        if not quiet:
            logger.info(f"Initialized BibliographyProcessor for {bib_file}")
            logger.info(f"Output directory: {self.output_dir}")
            if self.dry_run:
                logger.info("DRY RUN - no files will be modified")
            else:
                logger.debug("Database initialized successfully")

    def __enter__(self):
        """Context manager entry point - opens database connection."""
        if not self.dry_run:
            self.db_conn = sqlite3.connect(self.db_path)
            cursor = self.db_conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS processed_items (
                    citation_key TEXT PRIMARY KEY,
                    file_hashes TEXT,
                    last_processed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    dir_hash TEXT
                )
            """)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit point - closes database connection."""
        if not self.dry_run:
            if hasattr(self, 'db_conn'):
                self.db_conn.close()
        if exc_type:
            raise

    def _compute_file_hash(self, filepath: str) -> str:
        """Compute SHA-256 hash of a file.
        
        Args:
            filepath: Path to the file to hash
            
        Returns:
            str: Hex digest of the file's SHA-256 hash, or empty string on error
        """
        try:
            with open(filepath, 'rb') as f:
                return hashlib.sha256(f.read()).hexdigest()
        except Exception as e:
            logger.error(f"Failed to compute hash for {filepath}: {e}\n{traceback.format_exc()}")
            return ""

    def _compute_dir_hash(self, directory: Path) -> str:
        """Compute a hash of a directory's contents.
        
        This function hashes:
        - The relative paths of all files
        - For regular files: their contents
        - For symbolic links: their target paths (not the linked content)
        
        Args:
            directory: Path to the directory to hash
            
        Returns:
            str: Hex digest of the directory's SHA-256 hash, or empty string if directory doesn't exist
        """
        if not directory.exists():
            return ""
        
        # Get all files in directory, including symlinks
        files = sorted(f for f in directory.glob('**/*') if f.is_file() or f.is_symlink())
        hasher = hashlib.sha256()
        
        for file_path in files:
            try:
                # Add relative path to hash
                rel_path = file_path.relative_to(directory)
                hasher.update(str(rel_path).encode())
                
                if file_path.is_symlink():
                    # For symlinks, hash only the target path string
                    # This ensures the hash only changes if the symlink target changes
                    target_path = os.readlink(file_path)
                    hasher.update(str(target_path).encode())
                else:
                    # For regular files, hash the contents
                    with open(file_path, 'rb') as f:
                        for chunk in iter(lambda: f.read(4096), b''):
                            hasher.update(chunk)
            except Exception as e:
                logger.error(f"Failed to hash file {file_path}: {e}\n{traceback.format_exc()}")
                
        return hasher.hexdigest()

    def _parse_file_field(self, file_field: str) -> List[Path]:
        """Parse the file field from bibtex entry.
        
        Handles both standard file paths and Zotero-style file fields
        (description:filepath format).
        
        Args:
            file_field: The file field string from bibtex entry
            
        Returns:
            List[Path]: List of Path objects for files that exist on the system
        """
        if not file_field:
            return []
        
        paths = []
        for f in file_field.split(';'):
            try:
                if ':' in f:
                    # Handle Zotero-style file fields (description:filepath)
                    _, file_path = f.split(':', 1)
                else:
                    file_path = f
                    
                file_path = file_path.strip()
                if not file_path:
                    continue
                    
                path = Path(file_path)
                if path.exists():
                    logger.debug(f"Found file at: {path}")
                    paths.append(path)
                else:
                    logger.warning(f"Could not find file: {file_path}")
            except Exception as e:
                logger.error(f"Failed to parse file field entry '{f}': {e}\n{traceback.format_exc()}")
        
        return paths

    def process_all(self, force: bool = False, num_processes: int = None):
        """Process all entries in the bibliography file.
        
        Args:
            force: Whether to force reprocessing of all entries
            num_processes: Number of parallel processes to use (default: number of CPU cores)
        """
        try:
            with open(self.bib_file, 'r', encoding='utf-8') as bibtex_file:
                bib_database = bibtexparser.load(bibtex_file)
            
            # Determine which entries need processing
            entries_to_process = []
            total = len(bib_database.entries)
            
            if self.dry_run:
                # In dry-run mode, show all entries that would be processed
                for entry in bib_database.entries:
                    citation_key = entry.get('ID')
                    if not citation_key:
                        logger.warning("Entry missing citation key, skipping")
                        continue
                    
                    file_field = entry.get('file', '')
                    file_paths = self._parse_file_field(file_field)
                    if file_paths:
                        logger.info(f"Would process {citation_key}:")
                        for path in file_paths:
                            if path.exists():
                                logger.info(f"  - {path}")
                            else:
                                logger.warning(f"  - {path} (not found)")
                return
            
            if force:
                entries_to_process = bib_database.entries
            else:
                cursor = self.db_conn.cursor()
                for entry in bib_database.entries:
                    citation_key = entry.get('ID')
                    if not citation_key:
                        logger.warning("Entry missing citation key, skipping")
                        continue
                        
                    # Get current file hashes
                    file_paths = self._parse_file_field(entry.get('file', ''))
                    current_hashes = {
                        str(path): self._compute_file_hash(str(path))
                        for path in file_paths
                        if path.exists()
                    }
                    
                    entry_dir = self.output_dir / citation_key
                    dir_hash = self._compute_dir_hash(entry_dir)
                    
                    # Check if entry needs processing by comparing hashes
                    cursor.execute(
                        "SELECT file_hashes, dir_hash FROM processed_items WHERE citation_key = ?",
                        (citation_key,)
                    )
                    result = cursor.fetchone()
                    
                    if not result or (
                        json.loads(result[0] or '{}') != current_hashes or 
                        result[1] != dir_hash
                    ):
                        entries_to_process.append(entry)
            
            total = len(entries_to_process)
            logger.info(f"Found {total} entries to process")
            
            if not entries_to_process:
                logger.info("No entries need processing")
                return
            
            if num_processes is None:
                num_processes = multiprocessing.cpu_count()
            
            # Process entries using process_map with progress bar
            results = process_map(
                standalone_process_entry,
                [(entry, self.output_dir) for entry in entries_to_process],
                max_workers=num_processes,
                desc="Processing library",
                unit="entry"
            )
            
            # Update database with results
            processed = 0
            failed = 0
            for result in results:
                if result.success:
                    cursor = self.db_conn.cursor()
                    cursor.execute(
                        """
                        INSERT OR REPLACE INTO processed_items 
                        (citation_key, file_hashes, dir_hash) 
                        VALUES (?, ?, ?)
                        """,
                        (result.citation_key, json.dumps(result.file_hashes), result.dir_hash)
                    )
                    self.db_conn.commit()  # Commit after each successful entry
                    processed += 1
                else:
                    failed += 1
            
            logger.info(f"Processed {processed}/{total} entries successfully ({failed} failed)")
            
        except Exception as e:
            logger.error(f"Failed to process bibliography: {e}\n{traceback.format_exc()}")
            raise

def process_bibliography(bib_file: str, force: bool = False):
    """Process a bibliography file, converting all PDF attachments to markdown.
    
    Args:
        bib_file: Path to the bibliography file to process
        force: Whether to force reprocessing of all entries
    """
    with BibliographyProcessor(bib_file) as processor:
        processor.process_all(force=force)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Process bibliography files to markdown')
    parser.add_argument('bib_file', help='Path to bibliography file')
    parser.add_argument('--force', '-f', action='store_true', 
                       help='Force reprocessing of all entries')
    args = parser.parse_args()
    
    process_bibliography(args.bib_file, force=args.force)