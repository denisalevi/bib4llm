import argparse
import logging
import shutil
import multiprocessing
import sys
from datetime import datetime
from pathlib import Path
from .process_bibliography import BibliographyProcessor, DirectoryProcessor
from .watcher import watch_bibtex, watch_pdf, watch_directory

# Create logger at module level
logger = logging.getLogger(__name__)

def setup_logging(debug: bool, quiet: bool, input_path: Path, log_file: Path = None):
    """Set up logging configuration with separate handlers for console and file.
    
    Args:
        debug: Whether to show debug messages in console
        quiet: Whether to suppress info messages in console
        input_path: Path to the input file or directory, used to determine log file location
        log_file: Optional path to log file. If not provided, will use default location
    """
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)  # Capture all levels for handlers to filter
    
    # Clear any existing handlers from root logger
    root_logger.handlers.clear()
    
    # Set watchdog loggers to WARNING level to prevent debug messages
    logging.getLogger('watchdog').setLevel(logging.WARNING)
    
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
        log_dir = BibliographyProcessor.get_output_dir(input_path)
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
        description="Convert BibTeX library attachments or PDF files into LLM-readable format"
    )
    
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Convert command
    convert_parser = subparsers.add_parser(
        'convert',
        help="Convert BibTeX file, PDF file, or directory once"
    )
    convert_parser.add_argument(
        'input_path',
        type=Path,
        help="Path to the BibTeX file, PDF file, or directory to process"
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
    convert_parser.add_argument(
        '--no-recursive', '-R',
        action='store_true',
        help="Disable recursive processing of directories (only applicable if input is a directory)"
    )

    # Watch command
    watch_parser = subparsers.add_parser(
        'watch',
        help="Watch BibTeX file, PDF file, or directory for changes and convert automatically"
    )
    watch_parser.add_argument(
        'input_path',
        type=Path,
        help="Path to the BibTeX file, PDF file, or directory to watch"
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
    watch_parser.add_argument(
        '--no-recursive', '-R',
        action='store_true',
        help="Disable recursive watching of directories (only applicable if input is a directory)"
    )

    # Clean command
    clean_parser = subparsers.add_parser(
        'clean',
        help="Remove generated data directory for a BibTeX file or PDF file"
    )
    clean_parser.add_argument(
        'input_path',
        type=Path,
        help="Path to the BibTeX file or PDF file whose generated data should be removed"
    )
    clean_parser.add_argument(
        '--dry-run', '-n',
        action='store_true',
        help="Show what would be removed without actually doing it"
    )

    args = parser.parse_args()
    
    # Validate input path
    input_path = Path(args.input_path).resolve()
    if not input_path.exists():
        logger.error(f"Input path not found: {input_path}")
        sys.exit(1)
    
    # Set up logging before anything else
    setup_logging(
        debug=args.debug if hasattr(args, 'debug') else False,
        quiet=args.quiet if hasattr(args, 'quiet') else False,
        input_path=input_path,
        log_file=BibliographyProcessor.get_log_file(input_path) if not input_path.is_dir() else None
    )
    
    # Log the command that was run
    command_line = ' '.join(sys.argv)
    logger.debug(f"Running command: {command_line}")

    # Determine input type and call appropriate functions
    if input_path.is_dir():
        # Handle directory
        if args.command == 'convert':
            if args.dry_run:
                processor = DirectoryProcessor(input_path, dry_run=True, quiet=args.quiet)
                processor.process_directory(
                    recursive=not args.no_recursive,
                    force=args.force if hasattr(args, 'force') else False,
                    num_processes=args.processes
                )
            else:
                processor = DirectoryProcessor(input_path, quiet=args.quiet)
                processor.process_directory(
                    recursive=not args.no_recursive,
                    force=args.force if hasattr(args, 'force') else False,
                    num_processes=args.processes
                )
        elif args.command == 'watch':
            watch_directory(
                input_path,
                recursive=not args.no_recursive,
                num_processes=args.processes
            )
        elif args.command == 'clean':
            logger.error("Clean command is not supported for directories")
            sys.exit(1)
            
    elif BibliographyProcessor.is_pdf_file(input_path):
        # Handle PDF file
        if args.command == 'convert':
            if args.dry_run:
                with BibliographyProcessor(input_path, dry_run=True, quiet=args.quiet) as processor:
                    processor.process_all(force=args.force if hasattr(args, 'force') else False)
            else:
                with BibliographyProcessor(input_path, quiet=args.quiet) as processor:
                    processor.process_all(force=args.force if hasattr(args, 'force') else False)
        elif args.command == 'watch':
            watch_pdf(input_path, num_processes=args.processes)
        elif args.command == 'clean':
            output_dir = BibliographyProcessor.get_output_dir(input_path)
            if output_dir.exists():
                if args.dry_run:
                    logging.info(f"Would remove output directory: {output_dir}")
                else:
                    logging.info(f"Removing output directory: {output_dir}")
                    shutil.rmtree(output_dir)
            else:
                logging.info(f"No output directory found for {input_path}")
                
    elif input_path.suffix.lower() in ['.bib', '.bibtex']:
        # Handle BibTeX file
        if args.command == 'convert':
            if args.dry_run:
                with BibliographyProcessor(input_path, dry_run=True, quiet=args.quiet) as processor:
                    processor.process_all(
                        force=args.force if hasattr(args, 'force') else False,
                        num_processes=args.processes
                    )
            else:
                with BibliographyProcessor(input_path, quiet=args.quiet) as processor:
                    processor.process_all(
                        force=args.force if hasattr(args, 'force') else False,
                        num_processes=args.processes
                    )
        elif args.command == 'watch':
            watch_bibtex(input_path, num_processes=args.processes)
        elif args.command == 'clean':
            output_dir = BibliographyProcessor.get_output_dir(input_path)
            if output_dir.exists():
                if args.dry_run:
                    logging.info(f"Would remove output directory: {output_dir}")
                else:
                    logging.info(f"Removing output directory: {output_dir}")
                    shutil.rmtree(output_dir)
            else:
                logging.info(f"No output directory found for {input_path}")
    else:
        logger.error(f"Unsupported file type: {input_path}")
        sys.exit(1)

if __name__ == '__main__':
    main() 