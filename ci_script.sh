#!/bin/bash
set -e

# Install dependencies
pip install -r requirements.txt

# Run linting
flake8 oc_lettings_site/


# Run tests
pytest

# Check test coverage
coverage run -m pytest
coverage report -m
