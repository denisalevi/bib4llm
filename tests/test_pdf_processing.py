"""Test the PDF processing functionality."""

import unittest
import tempfile
import shutil
import logging
import multiprocessing
import subprocess
from pathlib import Path

from bib4llm.process_bibliography import DirectoryProcessor


class TestPDFProcessing(unittest.TestCase):
    """Test the PDF processing functionality."""

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
        
        # Path to a sample PDF file
        self.sample_pdf = Path("examples/pdf_dir/Cook - 2023 - A Geometric Framework for Odor Representation.pdf")
        
        # Skip if the sample PDF doesn't exist
        if not self.sample_pdf.exists():
            self.skipTest("Sample PDF file not found, skipping test")
        
        # Copy the sample PDF to the temporary directory
        self.temp_pdf = Path(self.temp_dir) / self.sample_pdf.name
        shutil.copy2(self.sample_pdf, self.temp_pdf)

    def tearDown(self):
        """Clean up after the test."""
        # Restore original logging handlers
        self.root_logger.removeHandler(self.null_handler)
        for handler in self.old_handlers:
            self.root_logger.addHandler(handler)

    def test_pdf_processing(self):
        """
        Test that a single PDF file can be processed correctly.
        
        This test:
        1. Copies a sample PDF to a temporary directory
        2. Processes the PDF using DirectoryProcessor
        3. Checks that the output files are created correctly
        """
        # Create the output directory
        output_dir = Path(self.temp_dir) / "output"
        output_dir.mkdir(exist_ok=True)
        
        # Process the PDF using DirectoryProcessor
        processor = DirectoryProcessor(self.temp_dir)
        
        # Override the output directory to use our temporary directory
        processor.output_dir = output_dir
        
        result = processor.process_directory()
        
        # Check that processing was successful
        self.assertTrue(result, "PDF processing should succeed")
        
        # Check that the output directory exists
        pdf_name = self.temp_pdf.stem
        pdf_output_dir = output_dir / pdf_name
        self.assertTrue(
            pdf_output_dir.exists(),
            f"PDF output directory {pdf_output_dir} should exist after processing, but it doesn't",
        )
        
        # Check that the markdown file exists
        md_file = pdf_output_dir / f"{pdf_name}.md"
        self.assertTrue(
            md_file.exists(),
            f"Markdown file {md_file} should exist after processing, but it doesn't",
        )
        
        # Check that the original PDF was copied
        pdf_file = pdf_output_dir / f"{pdf_name}.pdf"
        self.assertTrue(
            pdf_file.exists(),
            f"PDF file {pdf_file} should exist after processing, but it doesn't",
        )
        
        # Check that at least one image was extracted
        images = list(pdf_output_dir.glob("*.png"))
        self.assertTrue(
            len(images) > 0,
            f"No images were extracted for {pdf_name}",
        )
        
        # Check the content of the markdown file
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check that the markdown file contains the title
        self.assertIn("A Geometric Framework for Odor Representation", content,
                     "Markdown file should contain the PDF title")
        
        # Check that the markdown file contains image references
        self.assertIn("![", content,
                     "Markdown file should contain image references")

    def test_pdf_processing_with_custom_options(self):
        """
        Test PDF processing with force option.
        
        This test:
        1. Copies a sample PDF to a temporary directory
        2. Processes the PDF with force=True to ensure reprocessing
        3. Checks that the output is generated correctly
        """
        # Create the output directory
        output_dir = Path(self.temp_dir) / "output_force"
        output_dir.mkdir(exist_ok=True)
        
        # Process the PDF using DirectoryProcessor with force=True
        processor = DirectoryProcessor(self.temp_dir, dry_run=False)
        
        # Override the output directory to use our temporary directory
        processor.output_dir = output_dir
        
        result = processor.process_directory(force=True)
        
        # Check that processing was successful
        self.assertTrue(result is not None, "PDF processing with force option should succeed")
        
        # Check that the output directory exists
        pdf_name = self.temp_pdf.stem
        pdf_output_dir = output_dir / pdf_name
        self.assertTrue(
            pdf_output_dir.exists(),
            f"PDF output directory {pdf_output_dir} should exist after processing, but it doesn't",
        )
        
        # Process again to test force option
        processor = DirectoryProcessor(self.temp_dir, dry_run=False)
        result = processor.process_directory(force=True)
        
        # Check that processing was successful again
        self.assertTrue(result is not None, "PDF processing with force option should succeed on second run")


if __name__ == "__main__":
    unittest.main() 