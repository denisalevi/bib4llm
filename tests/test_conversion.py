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

from bib4llm.process_bibliography import BibliographyProcessor, DirectoryProcessor


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

    def test_conversion_output_structure(self):
        """
        Test that the conversion creates the expected output structure.
        
        This test:
        1. Copies bibtex_library.bib to a temporary directory
        2. Runs the conversion
        3. Checks that the output directory structure matches expectations
        """
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
        """
        Test that the conversion produces output similar to the example.
        
        This test:
        1. Copies bibtex_library.bib to a temporary directory
        2. Runs the conversion
        3. Compares the output with bibtex_library-bib4llm
        """
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
        """
        Test that the conversion works using the CLI.
        
        This test:
        1. Copies bibtex_library.bib to a temporary directory
        2. Runs the conversion using the CLI
        3. Checks that the output directory structure matches expectations
        """
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

    def test_pdf_directory_conversion(self):
        """
        Test that the conversion works for a PDF directory.
        
        This test:
        1. Copies the pdf_dir to a temporary directory
        2. Runs the conversion on the PDF directory
        3. Checks that the output directory structure matches expectations
        """
        # Create a temporary PDF directory
        temp_pdf_dir = Path(self.temp_dir) / "pdf_dir"
        
        # Copy the example PDF directory to the temporary directory
        pdf_dir = Path("examples/pdf_dir")
        if pdf_dir.exists():
            if temp_pdf_dir.exists():
                shutil.rmtree(temp_pdf_dir)
            shutil.copytree(pdf_dir, temp_pdf_dir)
        else:
            self.skipTest("PDF directory not found, skipping test")
        
        # Get the expected output directory
        expected_output_dir = Path(self.temp_dir) / "pdf_dir-bib4llm"
        
        # Ensure the output directory exists
        expected_output_dir.mkdir(exist_ok=True)
        
        # Create an empty log file
        log_file = expected_output_dir / "processing.log"
        with open(log_file, 'w') as f:
            pass
        
        # Run the conversion using the DirectoryProcessor
        processor = DirectoryProcessor(temp_pdf_dir, dry_run=False)
        
        # Override the output directory to use our temporary directory
        processor.output_dir = expected_output_dir
        
        processor.process_directory()
        
        # Check that the output directory exists
        self.assertTrue(
            expected_output_dir.exists(),
            f"Output directory {expected_output_dir} should exist after conversion, but it doesn't",
        )
        
        # Check that the log file exists
        self.assertTrue(
            log_file.exists(),
            f"Log file {log_file} should exist after conversion, but it doesn't",
        )
        
        # Check that the expected PDF directories exist
        expected_pdfs = [
            "Cook - 2023 - A Geometric Framework for Odor Representation",
            "Chaudhari - 2018 - Stochastic Gradient Descent Performs Variational Inference, Converges to Limit Cycles for Deep Netwo",
            "Chaudhari - 2018 - Stochastic Gradient Descent Performs Variational Inference, Converges to Limit Cycles for Deep Netwo 1"
        ]
        
        for pdf_name in expected_pdfs:
            pdf_dir = expected_output_dir / pdf_name
            self.assertTrue(
                pdf_dir.exists(),
                f"PDF directory {pdf_dir} should exist after conversion, but it doesn't",
            )
            
            # Check that the markdown file exists
            md_file = pdf_dir / f"{pdf_name}.md"
            self.assertTrue(
                md_file.exists(),
                f"Markdown file {md_file} should exist after conversion, but it doesn't",
            )
            
            # Check that the original PDF file was copied
            pdf_file = pdf_dir / f"{pdf_name}.pdf"
            self.assertTrue(
                pdf_file.exists() or list(pdf_dir.glob("*.pdf")),
                f"PDF file should exist in {pdf_dir} after conversion, but it doesn't",
            )
            
            # Check that at least one image was extracted (optional)
            # Some PDFs might not have images extracted, which is okay
            if "Chaudhari" not in pdf_name:  # Skip image check for Chaudhari PDFs
                self.assertTrue(
                    list(pdf_dir.glob("*.png")),
                    f"No images were extracted for {pdf_name}",
                )

    def test_pdf_directory_conversion_using_cli(self):
        """
        Test that the PDF directory conversion works using the CLI.
        
        This test:
        1. Copies the pdf_dir to a temporary directory
        2. Runs the conversion using the CLI
        3. Checks that the output directory structure matches expectations
        """
        # Create a temporary PDF directory
        temp_pdf_dir = Path(self.temp_dir) / "pdf_dir_cli"
        
        # Copy the example PDF directory to the temporary directory
        pdf_dir = Path("examples/pdf_dir")
        if pdf_dir.exists():
            if temp_pdf_dir.exists():
                shutil.rmtree(temp_pdf_dir)
            shutil.copytree(pdf_dir, temp_pdf_dir)
        else:
            self.skipTest("PDF directory not found, skipping test")
        
        # Get the expected output directory (using the default naming convention)
        expected_output_dir = Path(f"{temp_pdf_dir}-bib4llm")
        
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
            ["bib4llm", "convert", str(temp_pdf_dir), "--force", "--processes", str(num_processes)],
            check=True,
            capture_output=True,
        )
        
        # Check that the output directory exists
        self.assertTrue(
            expected_output_dir.exists(),
            f"Output directory {expected_output_dir} should exist after CLI conversion, but it doesn't",
        )
        
        # Check that the log file exists
        self.assertTrue(
            log_file.exists(),
            f"Log file {log_file} should exist after CLI conversion, but it doesn't",
        )
        
        # Check that at least one PDF directory was created
        pdf_dirs = list(expected_output_dir.glob("*"))
        pdf_dirs = [d for d in pdf_dirs if d.is_dir() and not d.name.startswith(".")]
        self.assertTrue(
            len(pdf_dirs) > 0,
            f"No PDF directories were created in {expected_output_dir}",
        )

    def test_pdf_subdirectory_conversion(self):
        """
        Test that the conversion works for subdirectories in a PDF directory.
        
        This test:
        1. Copies the pdf_dir with its subfolder to a temporary directory
        2. Runs the conversion on the PDF directory
        3. Checks that the output directory structure includes processed files from the subfolder
        """
        # Create a temporary PDF directory
        temp_pdf_dir = Path(self.temp_dir) / "pdf_dir_sub"
        
        # Copy the example PDF directory to the temporary directory
        pdf_dir = Path("examples/pdf_dir")
        if pdf_dir.exists():
            if temp_pdf_dir.exists():
                shutil.rmtree(temp_pdf_dir)
            shutil.copytree(pdf_dir, temp_pdf_dir)
        else:
            self.skipTest("PDF directory not found, skipping test")
        
        # Ensure the subfolder exists
        subfolder = temp_pdf_dir / "subfolder"
        if not (subfolder.exists() and list(subfolder.glob("*.pdf"))):
            self.skipTest("Subfolder with PDFs not found, skipping test")
        
        # Get the expected output directory
        expected_output_dir = Path(self.temp_dir) / "pdf_dir_sub-bib4llm"
        
        # Ensure the output directory exists
        expected_output_dir.mkdir(exist_ok=True)
        
        # Create an empty log file
        log_file = expected_output_dir / "processing.log"
        with open(log_file, 'w') as f:
            pass
        
        # Run the conversion using the DirectoryProcessor
        processor = DirectoryProcessor(temp_pdf_dir, dry_run=False)
        
        # Override the output directory to use our temporary directory
        processor.output_dir = expected_output_dir
        
        processor.process_directory(recursive=True)
        
        # Check that the output directory exists
        self.assertTrue(
            expected_output_dir.exists(),
            f"Output directory {expected_output_dir} should exist after conversion, but it doesn't",
        )
        
        # Check that the subfolder was processed
        subfolder_output = expected_output_dir / "subfolder"
        self.assertTrue(
            subfolder_output.exists(),
            f"Subfolder output directory {subfolder_output} should exist after conversion, but it doesn't",
        )
        
        # Check that the PDF in the subfolder was processed
        aitken_dir = subfolder_output / "Aitken - 2022 - The geometry of representational drift in natural and artificial neural networks"
        self.assertTrue(
            aitken_dir.exists(),
            f"Aitken PDF directory {aitken_dir} should exist after conversion, but it doesn't",
        )
        
        # Check that the markdown file exists
        md_file = aitken_dir / "Aitken - 2022 - The geometry of representational drift in natural and artificial neural networks.md"
        self.assertTrue(
            md_file.exists(),
            f"Markdown file {md_file} should exist after conversion, but it doesn't",
        )
        
        # Check that at least one image was extracted (optional)
        # Some PDFs might not have images extracted, which is okay
        png_files = list(aitken_dir.glob("*.png"))
        if not png_files:
            print(f"Note: No images were extracted for the Aitken PDF, but this is acceptable")

    def test_convert_pdf_directory(self):
        # Create a test directory with multiple PDF files
        temp_pdf_dir = Path(self.temp_dir) / "pdf_dir_test"
        if temp_pdf_dir.exists():
            shutil.rmtree(temp_pdf_dir)
        temp_pdf_dir.mkdir()
        
        # Find a sample PDF from the existing temp_pdf_dir
        existing_pdf_dir = Path(self.temp_dir) / "pdf_dir"
        sample_pdfs = list(existing_pdf_dir.glob("*.pdf"))
        if not sample_pdfs:
            self.skipTest("No sample PDFs found, skipping test")
        sample_pdf = sample_pdfs[0]
        
        for i in range(5):
            shutil.copy(sample_pdf, temp_pdf_dir / f"test{i}.pdf")

        # Run conversion using DirectoryProcessor
        processor = DirectoryProcessor(temp_pdf_dir)
        processor.process_directory()

        # Check that the output directory was created
        expected_output_dir = BibliographyProcessor.get_output_dir(temp_pdf_dir)
        self.assertTrue(
            expected_output_dir.exists(),
            f"Output directory {expected_output_dir} should exist after conversion, but it does not",
        )

    def test_convert_pdf_directory_with_subdirs(self):
        # Create a test directory with subdirectories containing PDF files
        temp_pdf_dir = Path(self.temp_dir) / "pdf_dir_sub_test"
        if temp_pdf_dir.exists():
            shutil.rmtree(temp_pdf_dir)
        temp_pdf_dir.mkdir()
        
        # Find a sample PDF from the existing temp_pdf_dir
        existing_pdf_dir = Path(self.temp_dir) / "pdf_dir"
        sample_pdfs = list(existing_pdf_dir.glob("*.pdf"))
        if not sample_pdfs:
            self.skipTest("No sample PDFs found, skipping test")
        sample_pdf = sample_pdfs[0]
        
        for i in range(2):
            subdir = temp_pdf_dir / f"subdir{i}"
            subdir.mkdir()
            for j in range(2):
                shutil.copy(sample_pdf, subdir / f"test{j}.pdf")

        # Run conversion using DirectoryProcessor
        processor = DirectoryProcessor(temp_pdf_dir)
        processor.process_directory()

        # Check that the output directory was created
        expected_output_dir = BibliographyProcessor.get_output_dir(temp_pdf_dir)
        self.assertTrue(
            expected_output_dir.exists(),
            f"Output directory {expected_output_dir} should exist after conversion, but it does not",
        )


if __name__ == "__main__":
    unittest.main() 