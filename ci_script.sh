#!/bin/bash
set -e

# Install dependencies
pip install -r requirements.txt

# Run linting
flake8 PROJECT-13/


# Run tests
pytest

# Check test coverage
coverage run -m pytest
coverage report -m
