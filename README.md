# Qaiko

An example package to demonstrate PyPI uploads.

## Installation
```bash
pip install qaiko
```

## Usage
```python
from qaiko import greet

print(greet("Python"))
```

Or from the command line:
```bash
qaiko                  # Hello, World!
qaiko --name Alice     # Hello, Alice!
qaiko --version        # Show version
```

## Development
```bash
pip install -e ".[dev]"
pytest                 # Run tests
ruff check src/        # Lint code
```
