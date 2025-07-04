"""
Tests for xzutils.core module.
"""

import pytest

from xzutils.core import example_tool, get_version, main


def test_get_version():
    """Test that get_version returns a string."""
    version = get_version()
    assert isinstance(version, str)
    assert version == "0.1.0"


def test_example_tool():
    """Test the example tool function."""
    result = example_tool()
    assert isinstance(result, str)
    assert "example tool" in result.lower()


def test_main(capsys):
    """Test the main function output."""
    main()
    captured = capsys.readouterr()
    assert "Hello from xzutils!" in captured.out
    assert "utility toolkit" in captured.out
