# bib4llm

Convert your BibTeX library attachments into LLM-readable format for AI-assisted research. This tool extracts text and figures from PDFs into markdown and PNG formats, making them indexable by AI coding assistants like Cursor AI. It does not perform any RAG (Retrieval-Augmented Generation) - that's left to downstream tools (e.g. Cursor AI, which indexes the active workspace folder).

## Features

- Extracts text and figures from PDF attachments into markdown and PNG formats using [PyMuPDF4LLM](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/)
- Watches BibTeX file for changes and automatically updates the converted files
- Developed with [Zotero](https://www.zotero.org/) + [BetterBibTeX](https://retorque.re/zotero-better-bibtex/) for [Cursor AI](https://www.cursor.com/) in mind, but may work with other reference managers' BibTeX exports (depending on their `file` field format) and for other LLM-based processing

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
The tool uses multiprocessing to process library entries in parallel. Depending on the number of papers in all of your attachments, the initial `convert` might take some time.

#### Command Options

##### `convert`
```bash
bib4llm convert <bibtex_file> [options]

Options:
  -f, --force      Force reprocessing of all entries
  -p, --processes  Number of parallel processes to use (default: number of CPU cores)
  -n, --dry-run    Show what would be processed without actually doing it
  -q, --quiet      Suppress all output except warnings and errors
  -d, --debug      Enable debug logging
```

##### `watch`
```bash
bib4llm watch <bibtex_file> [options]

Options:
  -p, --processes  Number of parallel processes to use (default: number of CPU cores)
  -q, --quiet      Suppress all output except warnings and errors
  -d, --debug      Enable debug logging
```

##### `clean`
```bash
bib4llm clean <bibtex_file> [options]

Options:
  -n, --dry-run    Show what would be removed without actually doing it
```

### Recommended Setup with Zotero for Cursor AI

1. Install Zotero and the BetterBibTeX extension
2. Create a collection for your project papers
3. (Optional) Configure BetterBibTeX to use your preferred citation key format (e.g. AuthorYYYY)
4. Export your collection with BetterBibTeX and enable automatic BibTeX file updates
5. Place the exported .bib file in your project
6. Run bib4llm to convert and watch for changes:
   ```bash
   bib4llm watch path/to/library.bib
   ```

The converted files will be stored in a directory named after your BibTeX file with a `-bib4llm` suffix (e.g., `library-bib4llm/` for `library.bib`). This directory can be indexed by Cursor AI or other tools for enhanced context during development.

### Future work
- Fix progress bar during convert (currently messed up due to tqdm + multiprocessing + logger logs)
- Develop a vscode extension to automatically start the `watch` call based on a per-workspace setting (which .bib file).
- Add support for other PDF extraction tools like llama-parse
