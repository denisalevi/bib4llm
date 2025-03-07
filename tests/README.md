# Tests for bib4llm

This directory contains unit tests for the bib4llm package.

## Running Tests

To run the tests, you can use pytest:

```bash
# Run all tests
pytest

# Run a specific test file
pytest tests/test_basic.py

# Run a specific test
pytest tests/test_basic.py::TestBibliographyProcessor::test_get_output_dir

# Run tests with verbose output
pytest -v

# Run tests with coverage report
pytest --cov=bib4llm
```

## Test Files

- `test_basic.py`: Basic tests for the core functionality
- `test_cli.py`: Tests for the command-line interface
- `test_conversion.py`: Tests for the conversion functionality
- `test_example_conversion.py`: Tests that compare the conversion output with the example output
- `test_process_bibliography.py`: Tests for the process_bibliography module

## Adding New Tests

When adding new tests, please follow these guidelines:

1. Create a new test file with the prefix `test_`.
2. Use the `unittest` framework for consistency.
3. Include docstrings for all test classes and methods.
4. Clean up any temporary files or directories created during tests.
5. Disable logging during tests to avoid cluttering the output. 