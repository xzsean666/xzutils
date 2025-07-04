"""
Core functionality of XZUtils.

This module contains the main entry point and core utilities.
"""


def main():
    """Main entry point for the xzutils package."""
    print("Hello from xzutils!")
    print("This is a utility toolkit that can be extended with various tools.")


def get_version():
    """Get the version of xzutils."""
    from . import __version__

    return __version__


# Example utility function - you can add more tools here
def example_tool():
    """An example utility function."""
    return "This is an example tool from xzutils!"


if __name__ == "__main__":
    main()
