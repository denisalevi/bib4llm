#!/bin/bash

# Script to run tests for bib4llm with optimized settings

# Default values
CORES="0-7"  # Only used when on zelos
PARALLEL="auto"
VERBOSE=false
COVERAGE=false

# Parse command line arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    --parallel=*)
      PARALLEL="${1#*=}"
      shift
      ;;
    --verbose|-v)
      VERBOSE=true
      shift
      ;;
    --coverage|-c)
      COVERAGE=true
      shift
      ;;
    --help|-h)
      echo "Usage: $0 [options] [test_files]"
      echo "Options:"
      echo "  --parallel=N      Number of parallel processes (default: auto)"
      echo "  --verbose, -v     Run tests in verbose mode"
      echo "  --coverage, -c    Generate coverage report"
      echo "  --help, -h        Show this help message"
      echo ""
      echo "Examples:"
      echo "  $0                           # Run all tests with default settings"
      echo "  $0 --parallel=4              # Use 4 parallel processes"
      echo "  $0 -v tests/test_basic.py    # Run specific tests verbosely"
      exit 0
      ;;
    *)
      # Assume remaining arguments are test files or pytest options
      break
      ;;
  esac
done

# Build the base command
if [[ "$(hostname)" == "zelos" ]]; then
  CMD="taskset -c $CORES python -m pytest"
else
  CMD="python -m pytest"
fi

# Build the pytest options
PYTEST_OPTS=""

# Add verbosity if requested
if $VERBOSE; then
  PYTEST_OPTS="$PYTEST_OPTS -v"
fi

# Add coverage if requested
if $COVERAGE; then
  PYTEST_OPTS="$PYTEST_OPTS --cov=bib4llm --cov-report=term"
fi

# Add parallel execution
PYTEST_OPTS="$PYTEST_OPTS -n $PARALLEL"

# Add any remaining arguments
if [[ $# -gt 0 ]]; then
  PYTEST_OPTS="$PYTEST_OPTS $@"
fi

# Combine command and options
CMD="$CMD $PYTEST_OPTS"

# Print the command being run
echo "Running: $CMD"

# Execute the command
eval $CMD 