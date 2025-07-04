# XZUtils

A versatile Python utility toolkit designed to be easily extensible with new tools and utilities.

## Features

- 🔧 Modular design for easy extension
- 📦 Simple installation from GitHub
- 🐍 Compatible with Python 3.8+
- 🚀 Ready-to-use utilities
- ⚡ Fast development with uv package manager

## Installation

### Using uv (Recommended)

```bash
# Install from GitHub
uv pip install git+https://github.com/yourusername/xzutils.git

# Or clone and install locally
git clone https://github.com/yourusername/xzutils.git
cd xzutils
uv pip install -e .

# Install with development dependencies
uv pip install -e .[dev]
```

### Using pip (Traditional)

```bash
# Install from GitHub
pip install git+https://github.com/yourusername/xzutils.git

# Local development installation
git clone https://github.com/yourusername/xzutils.git
cd xzutils
pip install -e .

# Install with development dependencies
pip install -e .[dev]
```

## Usage

### Command Line

After installation, you can use the `xzutils` command:

```bash
xzutils
```

### Python Import

```python
import xzutils

# Use the main function
xzutils.main()

# Use individual utilities
from xzutils.core import example_tool
result = example_tool()
print(result)

# Send Slack messages
from xzutils import sendMessage
response = sendMessage(
    webhook="https://hooks.slack.com/your-webhook-url",
    msg="Hello from xzutils!"
)
```

## Available Tools

### Message Utilities

- **Slack Messages**: Send messages to Slack channels via webhooks

  ```python
  from xzutils import sendMessage

  response = sendMessage(
      webhook="https://hooks.slack.com/your-webhook-url",
      msg="Your message here"
  )
  ```

### Core Utilities

- **Main function**: Basic entry point and version information
- **Example tools**: Template functions for adding new utilities

## Project Structure

```
xzutils/
├── xzutils/           # Main package directory
│   ├── __init__.py    # Package initialization
│   ├── core.py        # Core utilities
│   └── message/       # Message utilities
│       ├── __init__.py
│       └── slackMessage.py  # Slack messaging tools
├── tests/             # Test directory
│   ├── __init__.py
│   ├── test_core.py
│   └── test_message.py  # Message module tests
├── pyproject.toml     # Project configuration
├── README.md          # This file
├── LICENSE           # MIT License
├── .gitignore        # Git ignore rules
└── main.py           # Legacy entry point (deprecated)
```

## Adding New Tools

To add new utility tools to this package:

1. Create a new module in the `xzutils/` directory:

```python
# xzutils/my_new_tool.py
def my_utility_function():
    """A new utility function."""
    return "Hello from my new tool!"
```

2. Update `xzutils/__init__.py` to export your new tool:

```python
from .my_new_tool import my_utility_function

__all__ = [
    "main",
    "my_utility_function",
]
```

3. Users can then import and use your tool:

```python
from xzutils import my_utility_function
result = my_utility_function()
```

## Development

### Setting up development environment with uv

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone https://github.com/yourusername/xzutils.git
cd xzutils

# Install in development mode with all dependencies
uv pip install -e .[dev]
```

### Setting up development environment with pip

```bash
git clone https://github.com/yourusername/xzutils.git
cd xzutils
pip install -e .[dev]
```

### Running tests

```bash
# With uv
uv run pytest

# With traditional setup
pytest
```

### Code formatting

```bash
# With uv
uv run black xzutils/

# With traditional setup
black xzutils/
```

### Type checking

```bash
# With uv
uv run mypy xzutils/

# With traditional setup
mypy xzutils/
```

### Adding new dependencies

```bash
# With uv - automatically updates pyproject.toml
uv add requests  # for runtime dependency
uv add --dev pytest-cov  # for development dependency

# With traditional setup - manually edit pyproject.toml
# Then run: pip install -e .[dev]
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your utility tools
4. Write tests for your additions
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

### v0.1.0

- Initial release
- Basic package structure
- Example utility functions
- GitHub installation support
- uv package manager support
