# TDTU

A Python 3.13 project initialized with uv.

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd tdtu

# Create and activate the virtual environment
uv venv
.venv\Scripts\activate  # On Windows
# source .venv/bin/activate  # On Unix/macOS

# Install dependencies
uv pip install -e ".[dev]"
```

## Usage

```python
from tdtu.main import hello

message = hello("User")
print(message)  # Output: Hello, User!
```

## Development

This project uses:
- [uv](https://github.com/astral-sh/uv) for dependency management
- [pytest](https://docs.pytest.org/) for testing
- [black](https://black.readthedocs.io/) for code formatting
- [isort](https://pycqa.github.io/isort/) for import sorting
- [mypy](https://mypy.readthedocs.io/) for static type checking
- [ruff](https://github.com/astral-sh/ruff) for linting

## License

MIT
