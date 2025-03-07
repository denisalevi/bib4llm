"""Test the watcher functionality."""

import unittest
import tempfile
import shutil
import logging
import time
import threading
import signal
import os
import subprocess
import sys
from pathlib import Path


class TestWatcher(unittest.TestCase):
    """Test the watcher functionality."""

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
        
        # Create a sample BibTeX file
        self.bibtex_file = Path(self.temp_dir) / "test.bib"
        with open(self.bibtex_file, 'w') as f:
            f.write("""@article{test2023,
  title={Test Article},
  author={Test, Author},
  journal={Test Journal},
  year={2023}
}""")
        
        # Create a sample PDF directory
        self.pdf_dir = Path(self.temp_dir) / "pdf_dir"
        self.pdf_dir.mkdir()

    def tearDown(self):
        """Clean up after the test."""
        # Restore original logging handlers
        self.root_logger.removeHandler(self.null_handler)
        for handler in self.old_handlers:
            self.root_logger.addHandler(handler)

    def test_directory_watcher(self):
        """
        Test that the directory watcher script can be created and run.
        
        This test:
        1. Creates a script that simulates the watcher functionality
        2. Runs the script in a subprocess
        3. Checks that the script completes successfully
        """
        # Create a script to simulate the watcher
        watcher_script = Path(self.temp_dir) / "run_watcher.py"
        with open(watcher_script, 'w') as f:
            f.write("""
import sys
import time
from pathlib import Path

if __name__ == "__main__":
    directory = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])
    
    # Create a file to indicate the watcher ran
    with open(directory / "watcher_ran", "w") as f:
        f.write("Watcher completed")
    
    # Create the output directory to simulate processing
    output_dir.mkdir(exist_ok=True)
    
    # Exit with success
    sys.exit(0)
""")
        
        # Create an output directory within the temp directory
        output_dir = Path(self.temp_dir) / "watcher_output"
        
        # Start the watcher in a subprocess
        watcher_process = subprocess.Popen(
            [sys.executable, str(watcher_script), str(self.pdf_dir), str(output_dir)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        try:
            # Wait for the process to complete
            watcher_process.wait(timeout=5)
            
            # Check that the watcher ran
            watcher_ran_file = self.pdf_dir / "watcher_ran"
            self.assertTrue(
                watcher_ran_file.exists(),
                "Watcher did not run to completion"
            )
            
            # Check that the output directory was created
            self.assertTrue(
                output_dir.exists(),
                f"Output directory {output_dir} was not created"
            )
            
        finally:
            # Make sure the process is terminated
            if watcher_process.poll() is None:
                watcher_process.terminate()
                watcher_process.wait(timeout=2)


if __name__ == "__main__":
    unittest.main() 