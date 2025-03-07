import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging
import traceback
from .process_bibliography import BibliographyProcessor, DirectoryProcessor

# Create logger
logger = logging.getLogger(__name__)

class BibTexHandler(FileSystemEventHandler):
    def __init__(self, bib_file: Path, num_processes: int = None):
        self.bib_file = bib_file
        self.num_processes = num_processes
        self.last_processed = 0
        # Initial processing
        self._process()

    def on_modified(self, event):
        if not event.is_directory and Path(event.src_path) == self.bib_file:
            # Debounce to avoid multiple rapid processing
            current_time = time.time()
            if current_time - self.last_processed > 1:  # 1 second debounce
                self._process()
                self.last_processed = current_time

    def _process(self):
        """Process the bibliography file."""
        try:
            logger.debug(f"Processing {self.bib_file}")
            with BibliographyProcessor(self.bib_file) as processor:
                processor.process_all(num_processes=self.num_processes)
            logger.debug("Processing complete")
            logger.info(f"\nWatching BibTeX file: {self.bib_file.resolve()}\n")
        except FileNotFoundError as e:
            logger.error(f"Error processing {self.bib_file}: {e}\n{traceback.format_exc()}")
            # Exit the program when the file is not found
            raise SystemExit(1)
        except Exception as e:
            logger.error(f"Error processing {self.bib_file}: {e}\n{traceback.format_exc()}")
            logger.info(f"\nWatching BibTeX file: {self.bib_file.resolve()}\n")

class PDFHandler(FileSystemEventHandler):
    def __init__(self, pdf_file: Path, num_processes: int = None):
        self.pdf_file = pdf_file
        self.num_processes = num_processes
        self.last_processed = 0
        # Initial processing
        self._process()

    def on_modified(self, event):
        if not event.is_directory and Path(event.src_path) == self.pdf_file:
            # Debounce to avoid multiple rapid processing
            current_time = time.time()
            if current_time - self.last_processed > 1:  # 1 second debounce
                self._process()
                self.last_processed = current_time

    def _process(self):
        """Process the PDF file."""
        try:
            logger.debug(f"Processing PDF {self.pdf_file}")
            with BibliographyProcessor(self.pdf_file) as processor:
                result = processor.process_pdf(self.pdf_file)
            if result.success:
                logger.debug("Processing complete")
            else:
                logger.error(f"Failed to process PDF {self.pdf_file}")
            logger.info(f"\nWatching PDF file: {self.pdf_file.resolve()}\n")
        except FileNotFoundError as e:
            logger.error(f"Error processing {self.pdf_file}: {e}\n{traceback.format_exc()}")
            # Exit the program when the file is not found
            raise SystemExit(1)
        except Exception as e:
            logger.error(f"Error processing {self.pdf_file}: {e}\n{traceback.format_exc()}")
            logger.info(f"\nWatching PDF file: {self.pdf_file.resolve()}\n")

class DirectoryHandler(FileSystemEventHandler):
    def __init__(self, directory_path: Path, recursive: bool = True, num_processes: int = None):
        self.directory_path = directory_path
        self.recursive = recursive
        self.num_processes = num_processes
        self.last_processed = 0
        self.bibtex_extensions = ['.bib', '.bibtex']
        self.processor = DirectoryProcessor(directory_path)
        self.output_dir = BibliographyProcessor.get_output_dir(directory_path)
        # Initial processing
        self._process_directory()

    def on_created(self, event):
        """Handle file creation events."""
        file_path = Path(event.src_path)
        
        if event.is_directory:
            # If a directory is created and we're in recursive mode, we need to process it
            if self.recursive and file_path.is_relative_to(self.directory_path):
                self._process_directory()
        else:
            # Process new files based on their type
            self._process_file(file_path)

    def on_modified(self, event):
        """Handle file modification events."""
        if not event.is_directory:
            file_path = Path(event.src_path)
            # Process modified files based on their type
            self._process_file(file_path)
            
    def _process_file(self, file_path: Path):
        """Process a single file if it's a PDF or BibTeX file."""
        if not file_path.exists() or not file_path.is_file():
            return
            
        # Debounce to avoid multiple rapid processing
        current_time = time.time()
        if current_time - self.last_processed < 1:  # 1 second debounce
            return
            
        self.last_processed = current_time
        
        try:
            # Check if the file is a BibTeX file
            if file_path.suffix.lower() in self.bibtex_extensions:
                logger.debug(f"Processing BibTeX file: {file_path}")
                with BibliographyProcessor(file_path) as processor:
                    processor.process_all(num_processes=self.num_processes)
                logger.debug(f"Finished processing BibTeX file: {file_path}")
            
            # Check if the file is a PDF
            elif BibliographyProcessor.is_pdf_file(file_path):
                logger.debug(f"Processing PDF file: {file_path}")
                
                # Calculate the relative path from the directory being watched
                if file_path.is_relative_to(self.directory_path):
                    rel_path = file_path.relative_to(self.directory_path)
                    
                    # Create a DirectoryProcessor to handle the PDF with proper directory structure
                    processor = DirectoryProcessor(self.directory_path)
                    
                    # Create the output subdirectory
                    output_dir = Path(f"{self.directory_path}-bib4llm")
                    output_subdir = output_dir / rel_path.parent
                    output_subdir.mkdir(exist_ok=True, parents=True)
                    
                    # Create a custom output directory for this PDF
                    pdf_output_dir = output_subdir / file_path.stem
                    pdf_output_dir.mkdir(exist_ok=True, parents=True)
                    
                    # Process the PDF with the custom output directory
                    result = processor._process_pdf(file_path, pdf_output_dir)
                    
                    if result.success:
                        logger.debug(f"Finished processing PDF file: {file_path}")
                    else:
                        logger.error(f"Failed to process PDF file: {file_path}")
                else:
                    # If the file is not relative to the watched directory, process it directly
                    with BibliographyProcessor(file_path) as processor:
                        result = processor.process_pdf(file_path)
                    if result.success:
                        logger.debug(f"Finished processing PDF file: {file_path}")
                    else:
                        logger.error(f"Failed to process PDF file: {file_path}")
        except Exception as e:
            logger.error(f"Error processing file {file_path}: {e}\n{traceback.format_exc()}")
    
    def _process_directory(self):
        """Process the entire directory."""
        try:
            logger.debug(f"Processing directory {self.directory_path}")
            processor = DirectoryProcessor(self.directory_path)
            processor.process_directory(recursive=self.recursive, num_processes=self.num_processes)
            logger.debug("Directory processing complete")
            logger.info(f"\nWatching directory: {self.directory_path.resolve()}\n")
        except Exception as e:
            logger.error(f"Error processing directory {self.directory_path}: {e}\n{traceback.format_exc()}")
            logger.info(f"\nWatching directory: {self.directory_path.resolve()}\n")

def watch_bibtex(bib_file: Path, num_processes: int = None):
    """Watch a BibTeX file for changes and process it automatically.
    
    Args:
        bib_file: Path to the BibTeX file to watch
        num_processes: Number of parallel processes to use (default: number of CPU cores)
    """
    try:
        logger.info(f"\nWatching BibTeX file: {bib_file.resolve()}\n")
        event_handler = BibTexHandler(bib_file, num_processes)
        observer = Observer()
        observer.schedule(event_handler, str(bib_file.parent), recursive=False)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            logger.debug("Stopping file watcher")
            logger.info("\nStopped watching BibTeX file\n")
        
        observer.join()
    except Exception as e:
        logger.error(f"Error in watch_bibtex: {e}\n{traceback.format_exc()}")
        raise

def watch_pdf(pdf_file: Path, num_processes: int = None):
    """Watch a PDF file for changes and process it automatically.
    
    Args:
        pdf_file: Path to the PDF file to watch
        num_processes: Number of parallel processes to use (default: number of CPU cores)
    """
    try:
        logger.info(f"\nWatching PDF file: {pdf_file.resolve()}\n")
        event_handler = PDFHandler(pdf_file, num_processes)
        observer = Observer()
        observer.schedule(event_handler, str(pdf_file.parent), recursive=False)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            logger.debug("Stopping file watcher")
            logger.info("\nStopped watching PDF file\n")
        
        observer.join()
    except Exception as e:
        logger.error(f"Error in watch_pdf: {e}\n{traceback.format_exc()}")
        raise

def watch_directory(directory_path: Path, recursive: bool = True, num_processes: int = None):
    """Watch a directory for changes and process files automatically.
    
    Args:
        directory_path: Path to the directory to watch
        recursive: Whether to watch subdirectories recursively (default: True)
        num_processes: Number of parallel processes to use (default: number of CPU cores)
    """
    try:
        logger.info(f"\nWatching directory: {directory_path.resolve()}\n")
        event_handler = DirectoryHandler(directory_path, recursive, num_processes)
        observer = Observer()
        observer.schedule(event_handler, str(directory_path), recursive=recursive)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            logger.debug("Stopping directory watcher")
            logger.info("\nStopped watching directory\n")
        
        observer.join()
    except Exception as e:
        logger.error(f"Error in watch_directory: {e}\n{traceback.format_exc()}")
        raise 