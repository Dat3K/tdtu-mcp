"""Tests for the main module."""

from tdtu.main import hello


def test_hello_default() -> None:
    """Test the hello function with default arguments."""
    result = hello()
    assert result == "Hello, World!"


def test_hello_custom_name() -> None:
    """Test the hello function with a custom name."""
    result = hello("TDTU")
    assert result == "Hello, TDTU!"
