import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging
import traceback
from .process_bibliography import BibliographyProcessor

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