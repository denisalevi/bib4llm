"""Basic unit tests for bib4llm."""

import unittest
import tempfile
import shutil
import os
from pathlib import Path
import logging

from bib4llm.process_bibliography import BibliographyProcessor


class TestBibliographyProcessor(unittest.TestCase):
    """Test the BibliographyProcessor class."""
    
    def setUp(self):
        """Set up the test environment."""
        # Set up a null handler for logging instead of disabling it
        self.root_logger = logging.getLogger()
        self.old_handlers = self.root_logger.handlers.copy()
        self.root_logger.handlers.clear()
        self.null_handler = logging.NullHandler()
        self.root_logger.addHandler(self.null_handler)

    def tearDown(self):
        """Clean up after the test."""
        # Restore original logging handlers
        self.root_logger.removeHandler(self.null_handler)
        for handler in self.old_handlers:
            self.root_logger.addHandler(handler)

    def test_get_output_dir(self):
        """Test the get_output_dir method."""
        # Test with string path
        output_dir = BibliographyProcessor.get_output_dir("test.bib")
        self.assertEqual(
            output_dir.name,
            "test-bib4llm",
            f"Output directory name should be 'test-bib4llm' for 'test.bib', got '{output_dir.name}'",
        )
        
        # Test with Path object
        output_dir = BibliographyProcessor.get_output_dir(Path("test.bib"))
        self.assertEqual(
            output_dir.name,
            "test-bib4llm",
            f"Output directory name should be 'test-bib4llm' for Path('test.bib'), got '{output_dir.name}'",
        )
        
        # Test with Path object with directory
        output_dir = BibliographyProcessor.get_output_dir(Path("dir/test.bib"))
        self.assertEqual(
            output_dir.name,
            "test-bib4llm",
            f"Output directory name should be 'test-bib4llm' for Path('dir/test.bib'), got '{output_dir.name}'",
        )
        self.assertEqual(
            output_dir.parent.name,
            "dir",
            f"Parent directory name should be 'dir' for Path('dir/test.bib'), got '{output_dir.parent.name}'",
        )

    def test_get_log_file(self):
        """Test the get_log_file method."""
        # Test with string path
        log_file = BibliographyProcessor.get_log_file("test.bib")
        self.assertEqual(
            log_file.name,
            "processing.log",
            f"Log file name should be 'processing.log', got '{log_file.name}'",
        )
        self.assertEqual(
            log_file.parent.name,
            "test-bib4llm",
            f"Log file parent directory should be 'test-bib4llm', got '{log_file.parent.name}'",
        )
        
        # Test with Path object
        log_file = BibliographyProcessor.get_log_file(Path("test.bib"))
        self.assertEqual(
            log_file.name,
            "processing.log",
            f"Log file name should be 'processing.log', got '{log_file.name}'",
        )
        self.assertEqual(
            log_file.parent.name,
            "test-bib4llm",
            f"Log file parent directory should be 'test-bib4llm', got '{log_file.parent.name}'",
        )
        
        # Test with Path object with directory
        log_file = BibliographyProcessor.get_log_file(Path("dir/test.bib"))
        self.assertEqual(
            log_file.name,
            "processing.log",
            f"Log file name should be 'processing.log', got '{log_file.name}'",
        )
        self.assertEqual(
            log_file.parent.name,
            "test-bib4llm",
            f"Log file parent directory should be 'test-bib4llm', got '{log_file.parent.name}'",
        )
        self.assertEqual(
            log_file.parent.parent.name,
            "dir",
            f"Log file parent's parent directory should be 'dir', got '{log_file.parent.parent.name}'",
        )


if __name__ == "__main__":
    unittest.main() 