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
import pymupdf
import platform
from dataclasses import dataclass
from typing import Dict, List, Optional
from tqdm.contrib.concurrent import process_map

# Create logger
logger = logging.getLogger(__name__)

@dataclass
class ProcessingResult:
    """Result of processing a bibliography entry.
    
    Attributes:
        citation_key: The citation key from the bibliography entry
        file_hashes: Dictionary mapping file paths to their SHA-256 hashes
        dir_hash: Hash of the directory contents (excluding linked file contents)
        success: Whether the processing was successful
        mupdf_warning_count: Number of MuPDF warnings encountered during processing
    """
    citation_key: str
    file_hashes: Dict[str, str]
    dir_hash: str
    success: bool
    mupdf_warning_count: int = 0

def convert_to_extended_path(path: Path) -> Path:
    """Convert a path to Windows extended-length format if needed.
    
    Args:
        path: Path to convert
        
    Returns:
        Path: Converted path with extended-length format if on Windows and needed
    """
    if platform.system() == 'Windows':
        abs_path = path.resolve()
        path_str = str(abs_path)
        if len(path_str) > 259 and not path_str.startswith('\\\\?\\'):
            # Convert to extended path format
            return Path('\\\\?\\' + path_str)
    return path

def validate_windows_path(path: Path) -> Optional[str]:
    """Validate a path for Windows compatibility.
    
    Args:
        path: Path to validate
        
    Returns:
        Optional[str]: Error message if path is invalid, None if valid
    """
    # Convert to absolute path to check total length
    abs_path = path.resolve()
    
    if platform.system() == 'Windows':
        # Check if path can be handled with extended path format
        path_str = str(abs_path)
        if len(path_str) > 32767:  # Maximum length even with extended paths
            return f"Path exceeds maximum Windows extended path limit (32767 chars): {abs_path}"
        
        # Check for invalid characters in Windows filenames
        invalid_chars = '<>"|?*'
        filename = path.name
        if any(char in filename for char in invalid_chars):
            return f"Filename contains invalid Windows characters: {filename}"
    
    return None

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
    mupdf_warning_count = 0
    try:
        citation_key = entry.get('ID')
        if not citation_key:
            logger.warning("Entry missing citation key, skipping")
            return ProcessingResult(citation_key="", file_hashes={}, dir_hash="", success=False)
        
        entry_dir = output_dir / citation_key
        
        # Validate output directory path
        error = validate_windows_path(entry_dir)
        if error:
            logger.error(f"Invalid output directory path: {error}")
            return ProcessingResult(citation_key=citation_key, file_hashes={}, dir_hash="", success=False)
        
        entry_dir.mkdir(exist_ok=True, parents=True)
        processed_contents = []
        current_hashes = {}
        
        # Parse and validate files
        file_field = entry.get('file', '')
        logger.debug(f"File field for {citation_key}: {file_field}")
        
        # Helper functions needed by standalone_process_entry
        def parse_file_field(file_field: str) -> tuple[list[Path], int]:
            if not file_field:
                return [], 0
            
            paths = []
            not_found = 0
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
                        logger.debug(f"Could not find file: {file_path} for citation key: {citation_key}")
                        not_found += 1
                except Exception as e:
                    logger.error(f"Failed to parse file field entry '{f}': {e}\n{traceback.format_exc()}")
            
            return paths, not_found

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
        
        file_paths, not_found = parse_file_field(file_field)
        
        if not file_paths:
            logger.warning(f"No files found for entry {citation_key}")
            return ProcessingResult(citation_key=citation_key, file_hashes={}, dir_hash="", success=False)
        
        # Reset MuPDF warnings before processing files
        pymupdf.TOOLS.reset_mupdf_warnings()
        
        # Process files
        for file_path in file_paths:
            mime_type, _ = mimetypes.guess_type(file_path)
            
            if mime_type == 'application/pdf':
                # Process PDF and capture warnings/errors
                pymupdf.TOOLS.reset_mupdf_warnings()
                
                # Create a simplified link/copy of the PDF with just the citation key
                simple_pdf = entry_dir / f"{citation_key}.pdf"
                try:
                    if simple_pdf.exists() or simple_pdf.is_symlink():
                        simple_pdf.unlink()
                    simple_pdf.symlink_to(file_path.resolve())
                    logger.debug(f"Created symbolic link for processing: {simple_pdf} -> {file_path}")
                except OSError as e:
                    # If symlink fails (e.g., on Windows without admin rights), make a copy
                    logger.debug(f"Symlink failed, creating copy instead: {e}")
                    import shutil
                    shutil.copy2(file_path, simple_pdf)
                    logger.debug(f"Created copy for processing: {simple_pdf}")
                
                # Process PDF to markdown with images, using the simplified PDF path
                md_text = pymupdf4llm.to_markdown(
                    str(simple_pdf),
                    write_images=True,
                    image_path=str(entry_dir),
                    show_progress=False  # Disable pymupdf4llm progress bar
                )
                
                # Clean up the temporary copy if it was created (but keep symlinks)
                if simple_pdf.exists() and not simple_pdf.is_symlink():
                    simple_pdf.unlink()
                    logger.debug(f"Cleaned up temporary PDF copy: {simple_pdf}")
                
                # Check for warnings and write them to log
                warnings = pymupdf.TOOLS.mupdf_warnings()
                if warnings:
                    # Combine characters into complete messages
                    warning_messages = []
                    current_message = []
                    for char in warnings:
                        if char == '\n':
                            if current_message:
                                warning_messages.append(''.join(current_message))
                                current_message = []
                        else:
                            current_message.append(char)
                    if current_message:
                        warning_messages.append(''.join(current_message))
                    
                    mupdf_warning_count += len(warning_messages)
                    if warning_messages:
                        logger.debug(f"MuPDF warnings for '{file_path.name}': {";".join(warning_messages)}")
                
                processed_contents.append(md_text)
                logger.debug(f"Successfully processed PDF {file_path}")
            
            elif mime_type and mime_type.startswith('text/'):
                # Process text files by wrapping in markdown code blocks
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                file_type = file_path.suffix.lstrip('.')
                md_text = f"```{file_type}\n{content}\n```"
                processed_contents.append(md_text)
                logger.debug(f"Successfully processed text file {file_path}")
            else:
                logger.warning(f"Unsupported file type for {file_path}")
        
        if processed_contents:
            # Write combined markdown content with citation key header
            final_content = f"# Citation Key: {citation_key}\n\n---\n\n" + '\n\n---\n\n'.join(processed_contents)
            final_md = entry_dir / f"{citation_key}.md"
            
            # Validate markdown output path
            error = validate_windows_path(final_md)
            if error:
                logger.error(f"Invalid markdown output path: {error}")
                return ProcessingResult(citation_key=citation_key, file_hashes={}, dir_hash="", success=False)
            
            final_md.write_text(final_content, encoding='utf-8')
            
            # Compute hashes for change tracking
            current_hashes = {
                str(path): compute_file_hash(str(path))
                for path in file_paths
            }
        
        # Compute directory hash after all processing is done
        new_dir_hash = compute_dir_hash(entry_dir)
        logger.debug(f"Successfully processed entry {citation_key}")
        
        return ProcessingResult(
            citation_key=citation_key,
            file_hashes=current_hashes,
            dir_hash=new_dir_hash,
            success=True,
            mupdf_warning_count=mupdf_warning_count
        )
    except Exception as e:
        logger.error(f"Failed to process entry {citation_key}: {e}\n{traceback.format_exc()}")
        return ProcessingResult(
            citation_key=citation_key, 
            file_hashes={}, 
            dir_hash="", 
            success=False,
            mupdf_warning_count=mupdf_warning_count
        )

class BibliographyProcessor:
    @staticmethod
    def get_output_dir(bib_file: Path | str) -> Path:
        """Get the output directory path for a bibliography file.
        
        Args:
            bib_file: Path to the bibliography file
            
        Returns:
            Path to the output directory
        """
        bib_path = Path(bib_file).resolve()
        return (bib_path.parent / f"{bib_path.stem}-bib4llm").resolve()

    @staticmethod
    def get_log_file(bib_file: Path | str) -> Path:
        """Get the log file path for a bibliography file.
        
        Args:
            bib_file: Path to the bibliography file
            
        Returns:
            Path to the log file
        """
        return BibliographyProcessor.get_output_dir(bib_file) / "processing.log"

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
        self.output_dir = self.get_output_dir(self.bib_file)
        self.log_file = self.get_log_file(self.bib_file)
        
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

    def _parse_file_field(self, file_field: str) -> tuple[list[Path], int]:
        """Parse the file field from bibtex entry.
        
        Handles both standard file paths and Zotero-style file fields
        (description:filepath format).
        
        Args:
            file_field: The file field string from bibtex entry
            
        Returns:
            tuple: (List[Path], int) where:
                - List[Path] contains Path objects for files that exist
                - int is the count of files that were not found
        """
        if not file_field:
            return [], 0
        
        paths = []
        not_found = 0
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
                
                # Validate path for Windows compatibility
                error = validate_windows_path(path)
                if error:
                    logger.warning(f"Skipping invalid path: {error}")
                    not_found += 1
                    continue
                
                if path.exists():
                    logger.debug(f"Found file at: {path}")
                    paths.append(path)
                else:
                    logger.debug(f"Could not find file: {file_path}")
                    not_found += 1
            except Exception as e:
                logger.error(f"Failed to parse file field entry '{f}': {e}\n{traceback.format_exc()}")
        
        return paths, not_found

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
                    file_paths, missing = self._parse_file_field(entry.get('file', ''))
                    total_missing_files = missing
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
            total_mupdf_warnings = 0
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
                    self.db_conn.commit()
                    processed += 1
                    total_mupdf_warnings += result.mupdf_warning_count
                else:
                    failed += 1
            
            # After processing is complete, log summary
            summary_parts = []
            summary_parts.append(f"Processed {processed}/{total} entries successfully ({failed} failed)")
            if total_mupdf_warnings > 0:
                summary_parts.append(f"{total_mupdf_warnings} MuPDF warnings/errors occurred")
            if total_missing_files > 0:
                summary_parts.append(f"{total_missing_files} referenced files could not be found")
            
            logger.info(f"Processing complete: {', '.join(summary_parts)}. Check {self.log_file} for details.")
            
        except Exception as e:
            logger.error(f"Failed to process bibliography: {e}\n{traceback.format_exc()}")
            raise