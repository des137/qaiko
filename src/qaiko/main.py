import argparse


def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}! Welcome to my awesome package!"


def main():
    """Entry point for the application."""
    parser = argparse.ArgumentParser(
        description="A friendly greeting CLI",
        prog="qaiko",
    )
    parser.add_argument(
        "-n", "--name",
        default="World",
        help="Name to greet (default: World)",
    )
    parser.add_argument(
        "-v", "--version",
        action="store_true",
        help="Show version and exit",
    )
    args = parser.parse_args()

    if args.version:
        from qaiko import __version__
        print(f"qaiko {__version__}")
        return

    print(greet(args.name))


if __name__ == "__main__":
    main()
