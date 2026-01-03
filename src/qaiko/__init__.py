"""A simple example package."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("qaiko")
except PackageNotFoundError:
    __version__ = "0.0.0"  # fallback for development

from .main import greet

__all__ = ["greet", "__version__"]
