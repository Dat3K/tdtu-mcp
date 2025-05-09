"""Main module for the TDTU package."""

from typing import Any


def hello(name: str = "World") -> str:
    """Return a greeting message.
    
    Args:
        name: The name to greet. Defaults to "World".
        
    Returns:
        A greeting message.
    """
    return f"Hello, {name}!"


def main() -> None:
    """Run the main function."""
    message = hello()
    print(message)


if __name__ == "__main__":
    main()
