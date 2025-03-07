"""Test the process_bibliography module."""

import unittest
import tempfile
import shutil
import os
import sqlite3
from pathlib import Path
import logging

from bib4llm.process_bibliography import BibliographyProcessor, ProcessingResult


class TestProcessingResult(unittest.TestCase):
    """Test the ProcessingResult class."""

    def test_init(self):
        """Test initialization of ProcessingResult."""
        result = ProcessingResult(
            citation_key="test",
            file_hashes={"file1.pdf": "hash1", "file2.pdf": "hash2"},
            dir_hash="dirhash",
            success=True,
            mupdf_warning_count=2
        )
        
        self.assertEqual(
            result.citation_key,
            "test",
            f"ProcessingResult citation_key should be 'test', got '{result.citation_key}'",
        )
        self.assertEqual(
            result.file_hashes,
            {"file1.pdf": "hash1", "file2.pdf": "hash2"},
            f"ProcessingResult file_hashes should match the input dictionary, got {result.file_hashes}",
        )
        self.assertEqual(
            result.dir_hash,
            "dirhash",
            f"ProcessingResult dir_hash should be 'dirhash', got '{result.dir_hash}'",
        )
        self.assertTrue(
            result.success,
            f"ProcessingResult success should be True, got {result.success}",
        )
        self.assertEqual(
            result.mupdf_warning_count,
            2,
            f"ProcessingResult mupdf_warning_count should be 2, got {result.mupdf_warning_count}",
        )


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

    def test_init(self):
        """Test initialization of BibliographyProcessor."""
        processor = BibliographyProcessor(self.bib_file)
        self.assertEqual(
            processor.input_path,
            self.bib_file,
            f"BibliographyProcessor.input_path should match the input file, got '{processor.input_path}'",
        )
        self.assertEqual(
            processor.output_dir.name,
            "test-bib4llm",
            f"BibliographyProcessor.output_dir name should be 'test-bib4llm', got '{processor.output_dir.name}'",
        )
        self.assertFalse(
            processor.dry_run,
            f"BibliographyProcessor.dry_run should be False by default, got {processor.dry_run}",
        )
        
        # Check that the database file exists in the output directory
        db_file = processor.output_dir / "processed_files.db"
        self.assertTrue(
            db_file.exists(),
            f"Database file {db_file} should exist, but it doesn't",
        )
        
        # Clean up
        if hasattr(processor, 'db_conn'):
            processor.db_conn.close()

    def test_init_with_dry_run(self):
        """Test initialization of BibliographyProcessor with dry_run=True."""
        processor = BibliographyProcessor(self.bib_file, dry_run=True)
        self.assertEqual(
            processor.input_path,
            self.bib_file,
            f"BibliographyProcessor.input_path should match the input file, got '{processor.input_path}'",
        )
        self.assertEqual(
            processor.output_dir.name,
            "test-bib4llm",
            f"BibliographyProcessor.output_dir name should be 'test-bib4llm', got '{processor.output_dir.name}'",
        )
        self.assertTrue(
            processor.dry_run,
            f"BibliographyProcessor.dry_run should be True when set, got {processor.dry_run}",
        )
        
        # Clean up
        if hasattr(processor, 'db_conn'):
            processor.db_conn.close()

    def test_context_manager(self):
        """Test the context manager functionality."""
        with BibliographyProcessor(self.bib_file) as processor:
            self.assertEqual(
                processor.input_path,
                self.bib_file,
                f"BibliographyProcessor.input_path should match the input file, got '{processor.input_path}'",
            )
            self.assertEqual(
                processor.output_dir.name,
                "test-bib4llm",
                f"BibliographyProcessor.output_dir name should be 'test-bib4llm', got '{processor.output_dir.name}'",
            )
            self.assertFalse(
                processor.dry_run,
                f"BibliographyProcessor.dry_run should be False by default, got {processor.dry_run}",
            )
            
            # Check that the output directory was created
            self.assertTrue(
                processor.output_dir.exists(),
                f"Output directory {processor.output_dir} should exist, but it doesn't",
            )
            
            # Check that the database was created
            db_file = processor.output_dir / "processed_files.db"
            self.assertTrue(
                db_file.exists(),
                f"Database file {db_file} should exist, but it doesn't",
            )
            
            # Check that the database has the expected tables
            if hasattr(processor, 'db_conn'):
                cursor = processor.db_conn.cursor()
                tables = cursor.execute(
                    "SELECT name FROM sqlite_master WHERE type='table'"
                ).fetchall()
                table_names = [t[0] for t in tables]
                self.assertIn(
                    "processed_items",
                    table_names,
                    f"Database should contain a 'processed_items' table, got {table_names}",
                )


if __name__ == "__main__":
    unittest.main() 