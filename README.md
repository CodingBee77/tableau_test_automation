# Tableau Test Automation Framework

A skeleton framework for automating tests for Tableau reports.

## Overview

This project provides automated testing capabilities for Tableau reports, including API and UI testing.


## Layers

1. Clients
   API communication with Tableau Server

2. Pages
   UI Page Object Models

3. Tests
   Pytest test suites

4. Utils
   Shared helpers and services


## Project Structure

- **clients/** - Reusable Tableau client implementations
- **config/** - Configuration settings and environment variables
- **pages/** - Page objects for UI test automation
- **tests/api/** - API test suite and test cases
- **tests/ui/** - UI test suite and test cases
- **utils/** - Shared utility functions and helper modules

## Test Categories

- Smoke → Critical checks
- Regression → Functional validation
- Security → Permissions
- Data → Data accuracy

## Getting Started

### Prerequisites

Install required dependencies:

```bash
pip install -r requirements.txt
```

### Running Tests

```bash
# Run API tests
pytest api/

# Run UI tests
pytest ui/
```

## Status

This is a skeleton framework and is under development.

## License

