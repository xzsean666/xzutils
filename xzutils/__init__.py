"""
XZUtils - A collection of utility functions and classes.

A versatile Python toolkit that can be easily extended with new utility modules.
"""

__version__ = "0.1.1"
__author__ = "Your Name"
__email__ = "your.email@example.com"

# Import main utilities
from .core import main
from .message import sendMessage as slackMessage

# Define what gets imported with "from xzutils import *"
__all__ = [
    "main",
    "slackMessage",
]
