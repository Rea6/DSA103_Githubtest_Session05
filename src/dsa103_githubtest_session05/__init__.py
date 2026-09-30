from __future__ import annotations

import sys


def greetings(name: str) -> str:
    """Return a friendly greeting for the provided name."""
    return f"Hello {name}!"


def main() -> None:
    """Run the package CLI or prompt for a name."""
    if len(sys.argv) > 1:
        name = " ".join(sys.argv[1:])
    else:
        name = input("What is your name? ")
    print(greetings(name))


if __name__ == "__main__":
    main()
