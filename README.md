# bib4llm

Convert your BibTeX library attachments into LLM-readable format for AI-assisted research. This tool extracts text and figures from PDFs into markdown and PNG formats, making them indexable by AI coding assistants like Cursor AI. It does not perform any RAG (Retrieval-Augmented Generation) - that's left to downstream tools that can index the extracted content.

## Features

- Extracts text from PDF attachments into markdown format
- Converts figures, including vector graphics, to PNG format
- Watches BibTeX file for changes and automatically updates the converted files
- Developed with Zotero + BetterBibTeX in mind, but may work with other reference managers' BibTeX exports depending on their file path format

## Installation

```bash
pip install bib4llm
```

## Usage

### Command Line

```bash
# Convert a BibTeX file (one-time)
bib4llm convert path/to/library.bib [options]

# Watch a BibTeX file for changes and run convert at changes
bib4llm watch path/to/library.bib [options]

# Remove generated files
bib4llm clean path/to/library.bib [options]
```

### Command Options

#### Convert Command
```bash
bib4llm convert <bibtex_file> [options]

Options:
  -f, --force      Force reprocessing of all entries
  -p, --processes  Number of parallel processes to use (default: number of CPU cores)
  -n, --dry-run    Show what would be processed without actually doing it
  -q, --quiet      Suppress all output except warnings and errors
  -d, --debug      Enable debug logging
```

#### Watch Command
```bash
bib4llm watch <bibtex_file> [options]

Options:
  -p, --processes  Number of parallel processes to use (default: number of CPU cores)
  -q, --quiet      Suppress all output except warnings and errors
  -d, --debug      Enable debug logging
```

#### Clean Command
```bash
bib4llm clean <bibtex_file> [options]

Options:
  -n, --dry-run    Show what would be removed without actually doing it
```

### Recommended Setup with Zotero

1. Install Zotero and the BetterBibTeX extension
2. Create a collection for your project papers
3. Configure BetterBibTeX to use your preferred citation key format (e.g. AuthorYYYY)
4. Export your collection as BetterBibTeX and enable automatic BibTeX file updates
5. Place the exported .bib file in your project
6. Run bib4llm to convert and watch for changes:
   ```bash
   bib4llm watch path/to/library.bib
   ```

The converted files will be stored in a directory named after your BibTeX file with a `-bib4llm` suffix (e.g., `library-bib4llm/` for `library.bib`). This directory can be indexed by Cursor AI or other tools for enhanced context during development.