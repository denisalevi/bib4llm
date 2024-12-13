import argparse
import logging
import shutil
import multiprocessing
from pathlib import Path
from .process_bibliography import BibliographyProcessor
from .watcher import watch_bibtex

def setup_logging(debug: bool, quiet: bool):
    """Set up logging configuration."""
    if quiet:
        level = logging.WARNING
    else:
        level = logging.DEBUG if debug else logging.INFO
    
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

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
    setup_logging(args.debug if hasattr(args, 'debug') else False, 
                 args.quiet if hasattr(args, 'quiet') else False)

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
        output_dir = Path(f"{args.bibtex_file.stem}-bib4llm")
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