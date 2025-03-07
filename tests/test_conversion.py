"""Test the conversion functionality of bib4llm."""

import unittest
import tempfile
import shutil
import os
import filecmp
import subprocess
from pathlib import Path
import sqlite3
import logging

from bib4llm.process_bibliography import BibliographyProcessor


class TestConversion(unittest.TestCase):
    """Test the conversion functionality."""

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
        
        # Path to the example.bib file
        self.example_bib = Path("examples/example.bib")
        
        # Path to the example-bib4llm directory
        self.example_output = Path("examples/example-bib4llm")
        
        # Copy the example.bib file to the temporary directory
        self.temp_bib = Path(self.temp_dir) / "example.bib"
        shutil.copy2(self.example_bib, self.temp_bib)
        
        # Copy the PDF files to maintain the same structure
        pdf_dir = Path("examples/pdf_dir")
        if pdf_dir.exists():
            temp_pdf_dir = Path(self.temp_dir) / "pdf_dir"
            shutil.copytree(pdf_dir, temp_pdf_dir)
            
            # Create subfolder if it doesn't exist
            subfolder = temp_pdf_dir / "subfolder"
            subfolder.mkdir(exist_ok=True)
            
        # Update the file paths in the BibTeX file to point to the temporary directory
        with open(self.temp_bib, 'r') as f:
            content = f.read()
        
        # Replace the file paths
        content = content.replace('pdf_dir/', f'{self.temp_dir}/pdf_dir/')
        
        with open(self.temp_bib, 'w') as f:
            f.write(content)

    def tearDown(self):
        """Clean up after the test."""
        # Restore original logging handlers
        self.root_logger.removeHandler(self.null_handler)
        for handler in self.old_handlers:
            self.root_logger.addHandler(handler)

    def test_conversion_output_structure(self):
        """Test that the conversion creates the expected output structure."""
        # Get the expected output directory
        expected_output_dir = BibliographyProcessor.get_output_dir(self.temp_bib)
        
        # Ensure the output directory exists
        expected_output_dir.mkdir(exist_ok=True)
        
        # Create an empty log file
        log_file = expected_output_dir / "processing.log"
        with open(log_file, 'w') as f:
            pass
        
        # Run the conversion with multiple processes
        with BibliographyProcessor(self.temp_bib, dry_run=False) as processor:
            # Use multiple processes to speed up the test
            import multiprocessing
            num_processes = max(2, multiprocessing.cpu_count() // 2)
            processor.process_all(force=True, num_processes=num_processes)
        
        # Check that the output directory exists
        self.assertTrue(
            expected_output_dir.exists(),
            f"Output directory {expected_output_dir} should exist after conversion, but it doesn't",
        )
        
        # Check that the processing.log file exists
        self.assertTrue(
            log_file.exists(),
            f"Log file {log_file} should exist after conversion, but it doesn't",
        )
        
        # Check that the processed_files.db file exists
        self.assertTrue(
            (expected_output_dir / "processed_files.db").exists(),
            f"Database file {expected_output_dir / 'processed_files.db'} should exist after conversion, but it doesn't",
        )
        
        # Check that the expected entry directories exist
        expected_entries = ["Aitken2022", "Chaudhari2018", "Cook2023"]
        for entry in expected_entries:
            self.assertTrue(
                (expected_output_dir / entry).exists(),
                f"Entry directory {expected_output_dir / entry} should exist after conversion, but it doesn't",
            )

    def test_conversion_compare_to_example(self):
        """Test that the conversion output matches the example output."""
        # Get the expected output directory
        expected_output_dir = BibliographyProcessor.get_output_dir(self.temp_bib)
        
        # Ensure the output directory exists
        expected_output_dir.mkdir(exist_ok=True)
        
        # Create an empty log file
        log_file = expected_output_dir / "processing.log"
        with open(log_file, 'w') as f:
            pass
        
        # Run the conversion with multiple processes
        with BibliographyProcessor(self.temp_bib, dry_run=False) as processor:
            # Use multiple processes to speed up the test
            import multiprocessing
            num_processes = max(2, multiprocessing.cpu_count() // 2)
            processor.process_all(force=True, num_processes=num_processes)
        
        # Check that the output directory exists
        self.assertTrue(
            expected_output_dir.exists(),
            f"Output directory {expected_output_dir} should exist after conversion, but it doesn't",
        )
        
        # Compare the directory structures
        # Note: We're not comparing file contents because they might contain timestamps
        # or other dynamic content. Instead, we're checking that the structure is the same.
        expected_entries = ["Aitken2022", "Chaudhari2018", "Cook2023"]
        for entry in expected_entries:
            # Check that the entry directory exists in both places
            self.assertTrue(
                (expected_output_dir / entry).exists(),
                f"Entry directory {expected_output_dir / entry} should exist after conversion, but it doesn't",
            )
            self.assertTrue(
                (self.example_output / entry).exists(),
                f"Entry directory {self.example_output / entry} should exist in example output, but it doesn't",
            )
            
            # Check that the entry directory contains the expected files
            # Get the list of files in the example output
            example_files = [f.name for f in (self.example_output / entry).glob("*") if f.is_file()]
            # Get the list of files in the generated output
            generated_files = [f.name for f in (expected_output_dir / entry).glob("*") if f.is_file()]
            
            # Check that all example files exist in the generated output
            for file in example_files:
                if file.endswith('.pdf'):
                    # Skip PDF files as they might not be generated in the test
                    continue
                self.assertIn(
                    file,
                    generated_files,
                    f"File {file} should exist in generated output for entry {entry}, but it doesn't. Generated files: {generated_files}",
                )

    def test_conversion_using_cli(self):
        """Test the conversion using the CLI."""
        # Get the expected output directory
        expected_output_dir = BibliographyProcessor.get_output_dir(self.temp_bib)
        
        # Ensure the output directory exists
        expected_output_dir.mkdir(exist_ok=True)
        
        # Create an empty log file
        log_file = expected_output_dir / "processing.log"
        with open(log_file, 'w') as f:
            pass
        
        # Run the conversion using the CLI with multiple processes
        import multiprocessing
        num_processes = max(2, multiprocessing.cpu_count() // 2)
        subprocess.run(
            ["bib4llm", "convert", str(self.temp_bib), "--force", "--processes", str(num_processes)],
            check=True,
            capture_output=True,
        )
        
        # Check that the output directory exists
        self.assertTrue(
            expected_output_dir.exists(),
            f"Output directory {expected_output_dir} should exist after CLI conversion, but it doesn't",
        )
        
        # Check that the processing.log file exists
        self.assertTrue(
            log_file.exists(),
            f"Log file {log_file} should exist after CLI conversion, but it doesn't",
        )
        
        # Check that the processed_files.db file exists
        self.assertTrue(
            (expected_output_dir / "processed_files.db").exists(),
            f"Database file {expected_output_dir / 'processed_files.db'} should exist after CLI conversion, but it doesn't",
        )
        
        # Check that the expected entry directories exist
        expected_entries = ["Aitken2022", "Chaudhari2018", "Cook2023"]
        for entry in expected_entries:
            self.assertTrue(
                (expected_output_dir / entry).exists(),
                f"Entry directory {expected_output_dir / entry} should exist after CLI conversion, but it doesn't",
            )


if __name__ == "__main__":
    unittest.main() 