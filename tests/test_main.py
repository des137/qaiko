"""Tests for the qaiko package."""

from qaiko import greet, __version__


def test_greet_with_name():
    """Test greet function with a custom name."""
    result = greet("Alice")
    assert result == "Hello, Alice! Welcome to my awesome package!"


def test_greet_with_empty_string():
    """Test greet function with empty string."""
    result = greet("")
    assert result == "Hello, ! Welcome to my awesome package!"


def test_version_exists():
    """Test that version is defined."""
    assert __version__ is not None
    assert isinstance(__version__, str)
