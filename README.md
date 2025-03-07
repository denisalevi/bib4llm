# bib4llm

Convert your PDF library into LLM-readable format for AI-assisted research. This tool extracts text and figures from PDFs into markdown and PNG formats, making them indexable by AI coding assistants like Cursor AI. You can provide a directory with PDF files or a BibTeX file with PDF attachement paths in the `file` field to convert all of the attachments. The latter allows for automatic updating from e.g. a Zotero library. This tool does not perform any RAG (Retrieval-Augmented Generation) - that's left to downstream tools (e.g. Cursor AI, which indexes the active workspace folder).

## Features

- Reads PDF files in directory or `file` key in BibTex file to get paths of attachments
- Extracts text and figures from PDF attachments into markdown and PNG formats using [PyMuPDF4LLM](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/)
- Watches directories or BibTeX files for changes and automatically updates the converted files
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

# Convert a PDF file directly (one-time)
bib4llm convert path/to/paper.pdf [options]

# Convert all PDFs and BibTeX files in a directory
bib4llm convert path/to/directory [options]

# Watch a BibTeX file for changes and run convert when changes occur
bib4llm watch path/to/library.bib [options]

# Watch a PDF file for changes and run convert when changes occur
bib4llm watch path/to/paper.pdf [options]

# Watch a directory for changes (including new files) and convert accordingly
bib4llm watch path/to/directory [options]

# Remove generated files
bib4llm clean path/to/library.bib [options]
```
The tool uses multiprocessing to process library entries in parallel. Depending on the number of papers in all of your attachments, the initial `convert` might take some time.

#### Command Options

##### `convert`
```bash
bib4llm convert <input_path> [options]

Arguments:
  input_path            Path to the BibTeX file, PDF file, or directory to process

Options:
  -f, --force           Force reprocessing of all entries
  -p, --processes       Number of parallel processes to use (default: number of CPU cores)
  -n, --dry-run         Show what would be processed without actually doing it
  -q, --quiet           Suppress all output except warnings and errors
  -d, --debug           Enable debug logging
  -R, --no-recursive    Disable recursive processing of directories (only applicable if input is a directory)
```

##### `watch`
```bash
bib4llm watch <input_path> [options]

Arguments:
  input_path            Path to the BibTeX file, PDF file, or directory to watch

Options:
  -p, --processes       Number of parallel processes to use (default: number of CPU cores)
  -q, --quiet           Suppress all output except warnings and errors
  -d, --debug           Enable debug logging
  -R, --no-recursive    Disable recursive watching of directories (only applicable if input is a directory)
```

##### `clean`
```bash
bib4llm clean <input_path> [options]

Arguments:
  input_path            Path to the BibTeX file or PDF file whose generated data should be removed

Options:
  -n, --dry-run         Show what would be removed without actually doing it
```

### Setup with Zotero for Cursor AI

1. Install Zotero and the BetterBibTeX extension
2. Create a collection for your project papers
3. (Optional) Configure BetterBibTeX to use your preferred citation key format (e.g. AuthorYYYY)
4. Export your collection with BetterBibTeX and enable automatic BibTeX file updates
5. Place the exported .bib file in your project
6. Run bib4llm to convert and watch for changes:
   ```bash
   bib4llm watch path/to/library.bib
   ```

### Output Directory Structure

When processing a single PDF file:
```
paper.pdf -> paper-bib4llm/paper.md (and extracted images)
```

When processing a directory of PDF files, the directory structure is preserved:
```
pdf_dir/
├── paper1.pdf
└── subfolder/
    └── paper2.pdf

->

pdf_dir-bib4llm/
├── paper1/
│   ├── paper1.md
│   └── (extracted images)
└── subfolder/
    └── paper2/
        ├── paper2.md
        └── (extracted images)
```

For BibTeX files, each entry gets its own folder within the output directory:
```
bibtex_library.bib -> bibtex_library-bib4llm/
    ├── entry1/
    │   ├── entry1.md
    │   └── (extracted images)
    └── entry2/
        ├── entry2.md
        └── (extracted images)
```

### Future work
- Fix progress bar during convert (currently messed up due to tqdm + multiprocessing + logger logs)
- Develop a vscode extension to automatically start the `watch` call based on a per-workspace setting (which .bib file).
- Add support for other PDF extraction tools like llama-parse
