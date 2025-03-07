"""bib4llm - Extract text and figures from BibTeX library attachments into LLM-readable formats.

This package extracts content from PDF attachments in BibTeX entries into formats that can be easily
indexed by Large Language Models. It's particularly useful when working with AI coding assistants
like Cursor AI that can index your workspace but can't directly read PDFs.

The tool focuses solely on content extraction:
- Converts PDF text to markdown format
- Extracts figures and vector graphics as PNGs
- No RAG (Retrieval-Augmented Generation) - that's left to downstream tools

Developed with Zotero + BetterBibTeX in mind, but may work with other reference managers'
BibTeX exports depending on their file path format.

Now also supports:
- Direct processing of individual PDF files
- Processing entire directories of PDFs and BibTeX files
- Recursive directory scanning and watching
"""

__version__ = "0.1.0"

import pymupdf  # PyMuPDF
# Don't display MuPDF warnings and errors as messages (they are still stored in
# the warnings store)
pymupdf.TOOLS.mupdf_display_warnings(False)
pymupdf.TOOLS.mupdf_display_errors(False)
# Don't use Python's logging system for MuPDF messages, just collect them
#pymupdf.set_messages(False)

from .process_bibliography import BibliographyProcessor, DirectoryProcessor
from .watcher import watch_bibtex, watch_pdf, watch_directory

__all__ = [
    'BibliographyProcessor',
    'DirectoryProcessor',
    'watch_bibtex',
    'watch_pdf', 
    'watch_directory'
] 
