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
# Convert and watch a BibTeX file
bib4llm watch path/to/library.bib

# One-time conversion
bib4llm convert path/to/library.bib
```

### Recommended Setup with Zotero

1. Install Zotero and the BetterBibTeX extension
2. Create a collection for your project papers
3. Configure BetterBibTeX to:
   - Use your preferred citation key format (e.g., AuthorYYYY)
   - Enable automatic BibTeX file updates
4. Export your collection as BetterBibTeX
5. Place the exported .bib file in your project
6. Run bib4llm to convert and watch for changes:
   ```bash
   bib4llm watch path/to/library.bib
   ```

The converted files will be stored in a directory named after your BibTeX file with a `-bib4llm` suffix (e.g., `library-bib4llm/` for `library.bib`). This directory can be indexed by Cursor AI or other tools for enhanced context during development.

## VSCode Integration

Coming soon! A VSCode extension that will allow you to:
- Configure BibTeX files to watch
- View conversion status
- Trigger manual updates
- Preview converted content

## License

This project is licensed under the MIT License - see the LICENSE file for details. 