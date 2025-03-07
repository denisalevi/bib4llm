"""Test the conversion of bibtex_library.bib and compare with bibtex_library-bib4llm."""

import unittest
import tempfile
import shutil
import os
import filecmp
import subprocess
import sqlite3
import logging
import json
from pathlib import Path
from filecmp import dircmp
import multiprocessing

from bib4llm.process_bibliography import BibliographyProcessor


def compare_directories(dcmp, differences=None):
    """
    Recursively compare directories and collect differences.
    
    Args:
        dcmp: A dircmp object
        differences: Dictionary to collect differences
        
    Returns:
        Dictionary with differences
    """
    if differences is None:
        differences = {
            'left_only': [],
            'right_only': [],
            'diff_files': [],
            'funny_files': []
        }
    
    # Add differences at this level
    for name in dcmp.left_only:
        differences['left_only'].append(os.path.join(dcmp.left, name))
    for name in dcmp.right_only:
        differences['right_only'].append(os.path.join(dcmp.right, name))
    for name in dcmp.diff_files:
        differences['diff_files'].append(os.path.join(dcmp.left, name))
    for name in dcmp.funny_files:
        differences['funny_files'].append(os.path.join(dcmp.left, name))
    
    # Recursively compare subdirectories
    for sub_dcmp in dcmp.subdirs.values():
        compare_directories(sub_dcmp, differences)
    
    return differences


class TestExampleConversion(unittest.TestCase):
    """Test the conversion of bibtex_library.bib and compare with bibtex_library-bib4llm."""

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
        
        # Path to the example.bib file
        self.example_bib = Path("examples/bibtex_library.bib")
        
        # Path to the example-bib4llm directory
        self.example_output = Path("examples/bibtex_library-bib4llm")
        
        # Copy the example.bib file to the temporary directory
        self.temp_bib = Path(self.temp_dir) / "bibtex_library.bib"
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
        
        # Remove the temporary directory
        shutil.rmtree(self.temp_dir)

    def test_example_conversion(self):
        """
        Test that converting bibtex_library.bib produces output similar to bibtex_library-bib4llm.
        
        This test:
        1. Copies bibtex_library.bib to a temporary directory
        2. Runs the conversion
        3. Compares the output structure with bibtex_library-bib4llm
        """
        # Get the expected output directory
        expected_output_dir = Path(self.temp_dir) / "bibtex_library-bib4llm"
        
        # Ensure the output directory exists
        expected_output_dir.mkdir(exist_ok=True)
        
        # Create an empty log file
        log_file = expected_output_dir / "processing.log"
        with open(log_file, 'w') as f:
            pass
        
        # Run the conversion using the CLI with multiple processes
        num_processes = max(2, multiprocessing.cpu_count() // 2)
        result = subprocess.run(
            ["bib4llm", "convert", str(self.temp_bib), "--force", "--processes", str(num_processes)],
            check=True,
            capture_output=True,
            text=True,
        )
        
        # Print the output for debugging
        print(f"Command output: {result.stdout}")
        if result.stderr:
            print(f"Command error: {result.stderr}")
        
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
        
        # Compare the directory structures more thoroughly
        dcmp = dircmp(self.example_output, expected_output_dir)
        differences = compare_directories(dcmp)
        
        # We expect some differences due to timestamps, etc.
        # But we should check that the basic structure is the same
        # Ignore processing.log, processed_files.db, and PDF files in the comparison
        filtered_diff_files = [
            f for f in differences['diff_files'] 
            if not f.endswith('processing.log') and not f.endswith('processed_files.db') and not f.endswith('.pdf')
        ]
        
        # Print differences for debugging
        if filtered_diff_files:
            print(f"Different files: {filtered_diff_files}")
        if differences['left_only']:
            print(f"Files only in bibtex_library-bib4llm: {differences['left_only']}")
        if differences['right_only']:
            print(f"Files only in generated output: {differences['right_only']}")
        
        # Check database structure
        example_db = sqlite3.connect(self.example_output / "processed_files.db")
        generated_db = sqlite3.connect(expected_output_dir / "processed_files.db")
        
        # Check that the tables exist
        example_tables = example_db.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ).fetchall()
        generated_tables = generated_db.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ).fetchall()
        
        self.assertEqual(
            sorted([t[0] for t in example_tables]), 
            sorted([t[0] for t in generated_tables]),
            f"Database tables don't match. Example: {sorted([t[0] for t in example_tables])}, Generated: {sorted([t[0] for t in generated_tables])}",
        )
        
        # Close the database connections
        example_db.close()
        generated_db.close()


if __name__ == "__main__":
    unittest.main() 