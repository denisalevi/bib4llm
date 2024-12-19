import argparse
import logging
import shutil
import multiprocessing
import sys
from datetime import datetime
from pathlib import Path
from .process_bibliography import BibliographyProcessor
from .watcher import watch_bibtex

# Create logger at module level
logger = logging.getLogger(__name__)

def setup_logging(debug: bool, quiet: bool, bibtex_file: Path, log_file: Path = None):
    """Set up logging configuration with separate handlers for console and file.
    
    Args:
        debug: Whether to show debug messages in console
        quiet: Whether to suppress info messages in console
        bibtex_file: Path to the BibTeX file, used to determine log file location
        log_file: Optional path to log file. If not provided, will use default location
    """
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)  # Capture all levels for handlers to filter
    
    # Clear any existing handlers from root logger
    root_logger.handlers.clear()
    
    # Console handler with level based on arguments
    console_handler = logging.StreamHandler(sys.stdout)
    if quiet:
        console_handler.setLevel(logging.WARNING)
    elif debug:
        console_handler.setLevel(logging.DEBUG)
    else:
        console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    root_logger.addHandler(console_handler)
    
    # File handler always at DEBUG level
    if log_file is None:
        # Fallback to default location if no log_file provided
        log_dir = Path(f"{bibtex_file.stem}-bib4llm")
        log_dir.mkdir(exist_ok=True)
        log_file = log_dir / "processing.log"
    else:
        # Ensure log file's parent directory exists
        log_file.parent.mkdir(exist_ok=True)
        
    file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    root_logger.addHandler(file_handler)

def main():
    parser = argparse.ArgumentParser(
        description="Convert BibTeX library attachments into LLM-readable format"
    )
    
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Convert command
    convert_parser = subparsers.add_parser(
        'convert',
        help="Convert BibTeX file once"
    )
    convert_parser.add_argument(
        'bibtex_file',
        type=Path,
        help="Path to the BibTeX file"
    )
    convert_parser.add_argument(
        '--force', '-f',
        action='store_true',
        help="Force reprocessing of all entries"
    )
    convert_parser.add_argument(
        '--processes', '-p',
        type=int,
        default=multiprocessing.cpu_count(),
        help="Number of parallel processes to use (default: number of CPU cores)"
    )
    convert_parser.add_argument(
        '--dry-run', '-n',
        action='store_true',
        help="Show what would be processed without actually doing it"
    )
    convert_parser.add_argument(
        '--quiet', '-q',
        action='store_true',
        help="Suppress all output except warnings and errors"
    )
    convert_parser.add_argument(
        '--debug', '-d',
        action='store_true',
        help="Enable debug logging"
    )

    # Watch command
    watch_parser = subparsers.add_parser(
        'watch',
        help="Watch BibTeX file for changes and convert automatically"
    )
    watch_parser.add_argument(
        'bibtex_file',
        type=Path,
        help="Path to the BibTeX file to watch"
    )
    watch_parser.add_argument(
        '--processes', '-p',
        type=int,
        default=multiprocessing.cpu_count(),
        help="Number of parallel processes to use (default: number of CPU cores)"
    )
    watch_parser.add_argument(
        '--quiet', '-q',
        action='store_true',
        help="Suppress all output except warnings and errors"
    )
    watch_parser.add_argument(
        '--debug', '-d',
        action='store_true',
        help="Enable debug logging"
    )

    # Clean command
    clean_parser = subparsers.add_parser(
        'clean',
        help="Remove generated data directory for a BibTeX file"
    )
    clean_parser.add_argument(
        'bibtex_file',
        type=Path,
        help="Path to the BibTeX file whose generated data should be removed"
    )
    clean_parser.add_argument(
        '--dry-run', '-n',
        action='store_true',
        help="Show what would be removed without actually doing it"
    )

    args = parser.parse_args()
    
    # Set up logging before anything else
    setup_logging(
        debug=args.debug if hasattr(args, 'debug') else False,
        quiet=args.quiet if hasattr(args, 'quiet') else False,
        bibtex_file=args.bibtex_file,
        log_file=BibliographyProcessor.get_log_file(args.bibtex_file)
    )
    
    # Log the command that was run
    command_line = ' '.join(sys.argv)
    logger.debug(f"Running command: {command_line}")

    if args.command == 'convert':
        if args.dry_run:
            with BibliographyProcessor(args.bibtex_file, dry_run=True) as processor:
                processor.process_all(force=args.force, num_processes=args.processes)
        else:
            with BibliographyProcessor(args.bibtex_file) as processor:
                processor.process_all(force=args.force, num_processes=args.processes)
    elif args.command == 'watch':
        watch_bibtex(args.bibtex_file, num_processes=args.processes)
    elif args.command == 'clean':
        output_dir = BibliographyProcessor.get_output_dir(args.bibtex_file)
        if output_dir.exists():
            if args.dry_run:
                logging.info(f"Would remove output directory: {output_dir}")
            else:
                logging.info(f"Removing output directory: {output_dir}")
                shutil.rmtree(output_dir)
        else:
            logging.info(f"No output directory found for {args.bibtex_file}")

if __name__ == '__main__':
    main() 