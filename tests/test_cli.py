"""Test the CLI functionality of bib4llm."""

import unittest
import tempfile
import shutil
import os
import subprocess
from pathlib import Path
import logging
from bib4llm.process_bibliography import BibliographyProcessor, DirectoryProcessor


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
            "Convert BibTeX library attachments or PDF files",
            result.stdout,
            f"Help output should mention 'Convert BibTeX library attachments or PDF files', got: {result.stdout}",
        )

    def test_convert_help(self):
        """Test the convert help command."""
        result = subprocess.run(
            ["bib4llm", "convert", "--help"],
            check=True,
            capture_output=True,
            text=True,
        )
        # Check for the actual text in the help output
        self.assertIn(
            "Path to the BibTeX file, PDF file, or directory to",
            result.stdout,
            f"Convert help output should mention path to BibTeX/PDF/directory, got: {result.stdout}",
        )

    def test_watch_help(self):
        """Test the watch help command."""
        result = subprocess.run(
            ["bib4llm", "watch", "--help"],
            check=True,
            capture_output=True,
            text=True,
        )
        # Check for the actual text in the help output
        self.assertIn(
            "Path to the BibTeX file, PDF file, or directory to",
            result.stdout,
            f"Watch help output should mention path to BibTeX/PDF/directory, got: {result.stdout}",
        )

    def test_clean_help(self):
        """Test the clean help command."""
        result = subprocess.run(
            ["bib4llm", "clean", "--help"],
            check=True,
            capture_output=True,
            text=True,
        )
        # Check for partial match since the help text might have line breaks
        self.assertTrue(
            "Path to the BibTeX file" in result.stdout and "PDF file" in result.stdout and "generated data" in result.stdout and "removed" in result.stdout,
            f"Clean help output should mention path to BibTeX/PDF file and data removal, got: {result.stdout}",
        )

    def test_convert_dry_run(self):
        """Test the convert command with dry run."""
        # Make sure the output directory doesn't exist before the test
        output_dir = BibliographyProcessor.get_output_dir(self.bib_file)
        if output_dir.exists():
            shutil.rmtree(output_dir)
        
        result = subprocess.run(
            ["bib4llm", "convert", str(self.bib_file), "--dry-run"],
            check=True,
            capture_output=True,
            text=True,
        )
        
        # Check that the output contains the dry run message
        self.assertIn(
            "DRY RUN",
            result.stdout,
            "Output should contain 'DRY RUN' message"
        )
        
        # Check that the output contains the expected output directory
        self.assertIn(
            str(output_dir),
            result.stdout,
            f"Output should mention the output directory {output_dir}"
        )
        
        # Clean up the output directory if it was created despite the dry run
        if output_dir.exists():
            shutil.rmtree(output_dir)
            logging.warning(f"Output directory {output_dir} was created during dry run and had to be cleaned up")

    def test_convert_creates_output_dir(self):
        result = subprocess.run(
            ["bib4llm", "convert", str(self.bib_file)],
            check=True,
            capture_output=True,
            text=True,
        )
        # Check that the output directory was created
        output_dir = BibliographyProcessor.get_output_dir(self.bib_file)
        self.assertTrue(
            output_dir.exists(),
            f"Output directory {output_dir} should exist after conversion, but it does not",
        )

    def test_clean_removes_output_dir(self):
        # First create the output directory
        output_dir = BibliographyProcessor.get_output_dir(self.bib_file)
        output_dir.mkdir(parents=True, exist_ok=True)

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

    def test_processes_option(self):
        # Create a test directory with multiple PDF files
        test_dir = Path(self.temp_dir) / "test_processes"
        test_dir.mkdir()
        
        # Use a sample PDF from examples directory
        sample_pdf = Path("examples/pdf_dir/Cook - 2023 - A Geometric Framework for Odor Representation.pdf")
        if not sample_pdf.exists():
            self.skipTest("Sample PDF not found, skipping test")
        
        for i in range(5):
            shutil.copy(sample_pdf, test_dir / f"test{i}.pdf")

        # Run conversion with 2 processes
        result = subprocess.run(
            ["bib4llm", "convert", str(test_dir), "--processes", "2"],
            check=True,
            capture_output=True,
            text=True,
        )

        # Check that the output directory was created
        output_dir = BibliographyProcessor.get_output_dir(test_dir)
        self.assertTrue(
            output_dir.exists(),
            f"Output directory {output_dir} should exist after conversion, but it does not",
        )


if __name__ == "__main__":
    unittest.main() 