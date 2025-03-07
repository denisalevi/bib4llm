Here are some examples to see what `bib4llm` does. `bibtex_library.bib` is an example BibTex file with PDF attachment paths in the `file` field linking to attachements in the `pdf_dir` directory.

You can convert the BibTex file to a directory of markdown and PNG files, which will create the `bibtex_library-bib4llm` directory:
```bash
bib4llm convert bibtex_library.bib
```

You can also convert the directory of PDF files `pdf_dir` directly, which will create the `pdf_dir-bib4llm` directory:
```bash
bib4llm convert pdf_dir
```
