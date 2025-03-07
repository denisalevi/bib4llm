"""Test the CLI functionality of bib4llm."""

import unittest
import tempfile
import shutil
import os
import subprocess
from pathlib import Path
import logging


class TestCLI(unittest.TestCase):
    """Test the CLI functionality."""

    def setUp(self):
        """Set up the test environment."""
        # Set up a null handler for logging instead of disabling it
        self.root_logger = logging.getLogger()
        self.old_handlers = self.root_logger.handlers.copy()
        self.root_logger.handlers.clear()
        self.null_handler = logging.NullHandler()
        self.root_logger.addHandler(self.null_handler)
        
        # Create a temporary directory
        self.temp_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.temp_dir)
        
        # Create a simple BibTeX file
        self.bib_file = Path(self.temp_dir) / "test.bib"
        with open(self.bib_file, "w") as f:
            f.write("""@article{Test2023,
  title = {Test Article},
  author = {Test, Author},
  year = {2023},
  journal = {Test Journal},
  volume = {1},
  number = {1},
  pages = {1--10}
}
""")

    def tearDown(self):
        """Clean up after the test."""
        # Restore original logging handlers
        self.root_logger.removeHandler(self.null_handler)
        for handler in self.old_handlers:
            self.root_logger.addHandler(handler)

    def test_help(self):
        """Test the help command."""
        result = subprocess.run(
            ["bib4llm", "--help"],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "Convert BibTeX library attachments",
            result.stdout,
            f"Help output should mention 'Convert BibTeX library attachments', got: {result.stdout}",
        )

    def test_convert_help(self):
        """Test the convert help command."""
        result = subprocess.run(
            ["bib4llm", "convert", "--help"],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "Path to the BibTeX file",
            result.stdout,
            f"Convert help output should mention 'Path to the BibTeX file', got: {result.stdout}",
        )

    def test_watch_help(self):
        """Test the watch help command."""
        result = subprocess.run(
            ["bib4llm", "watch", "--help"],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "Path to the BibTeX file to watch",
            result.stdout,
            f"Watch help output should mention 'Path to the BibTeX file to watch', got: {result.stdout}",
        )

    def test_clean_help(self):
        """Test the clean help command."""
        result = subprocess.run(
            ["bib4llm", "clean", "--help"],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "Path to the BibTeX file whose generated data should be removed",
            result.stdout,
            f"Clean help output should mention 'Path to the BibTeX file whose generated data should be removed', got: {result.stdout}",
        )

    def test_convert_dry_run(self):
        """Test the convert command with dry run."""
        result = subprocess.run(
            ["bib4llm", "convert", str(self.bib_file), "--dry-run"],
            check=True,
            capture_output=True,
            text=True,
        )
        # Check that the output directory was not created
        output_dir = Path(f"{self.bib_file.stem}-bib4llm")
        self.assertFalse(
            output_dir.exists(),
            f"Output directory {output_dir} should not exist after dry run, but it does",
        )

    def test_clean(self):
        """Test the clean command."""
        # First create the output directory
        output_dir = Path(self.temp_dir) / f"{self.bib_file.stem}-bib4llm"
        output_dir.mkdir()
        
        # Run the clean command
        result = subprocess.run(
            ["bib4llm", "clean", str(self.bib_file)],
            check=True,
            capture_output=True,
            text=True,
        )
        
        # Check that the output directory was removed
        self.assertFalse(
            output_dir.exists(),
            f"Output directory {output_dir} should be removed after clean command, but it still exists",
        )

    def test_clean_dry_run(self):
        """Test the clean command with dry run."""
        # First create the output directory
        output_dir = Path(self.temp_dir) / f"{self.bib_file.stem}-bib4llm"
        output_dir.mkdir()
        
        # Run the clean command with dry run
        result = subprocess.run(
            ["bib4llm", "clean", str(self.bib_file), "--dry-run"],
            check=True,
            capture_output=True,
            text=True,
        )
        
        # Check that the output directory still exists
        self.assertTrue(
            output_dir.exists(),
            f"Output directory {output_dir} should still exist after clean dry run, but it doesn't",
        )

    def test_convert_with_processes(self):
        """Test the convert command with the --processes flag."""
        # Create a simple BibTeX file with a file field
        bib_file = Path(self.temp_dir) / "test_processes.bib"
        with open(bib_file, "w") as f:
            f.write("""@article{Test2023,
  title = {Test Article},
  author = {Test, Author},
  year = {2023},
  journal = {Test Journal},
  volume = {1},
  number = {1},
  pages = {1--10}
}
""")
        
        # Get the expected output directory
        output_dir = Path(self.temp_dir) / "test_processes-bib4llm"
        
        # Ensure the output directory exists
        output_dir.mkdir(exist_ok=True)
        
        # Create an empty log file
        log_file = output_dir / "processing.log"
        with open(log_file, 'w') as f:
            pass
        
        # Run the conversion using the CLI with multiple processes
        import multiprocessing
        num_processes = max(2, multiprocessing.cpu_count() // 2)
        result = subprocess.run(
            ["bib4llm", "convert", str(bib_file), "--force", "--processes", str(num_processes)],
            check=True,
            capture_output=True,
            text=True,
        )
        
        # Check that the output directory exists
        self.assertTrue(
            output_dir.exists(),
            f"Output directory {output_dir} should exist after conversion, but it doesn't",
        )
        
        # Check that the processing.log file exists
        self.assertTrue(
            log_file.exists(),
            f"Log file {log_file} should exist after conversion, but it doesn't",
        )
        
        # Check that the processed_files.db file exists
        self.assertTrue(
            (output_dir / "processed_files.db").exists(),
            f"Database file {output_dir / 'processed_files.db'} should exist after conversion, but it doesn't",
        )


if __name__ == "__main__":
    unittest.main() 