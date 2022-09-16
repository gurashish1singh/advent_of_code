import argparse
from importlib import import_module
from typing import Optional


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "year",
        choices=["twenty"],
        help="Advent of Code year",
    )
    parser.add_argument(
        "day",
        help="Advent of Code day"
    )
    args = parser.parse_args(argv)

    name = f"{args.year}.{args.day}"
    mod = import_module(name)
    mod.main()


if __name__ == "__main__":
    main()
