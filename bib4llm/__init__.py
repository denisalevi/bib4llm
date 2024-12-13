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
"""

__version__ = "0.1.0"

from .process_bibliography import BibliographyProcessor
from .watcher import watch_bibtex

__all__ = ['BibliographyProcessor', 'watch_bibtex'] 