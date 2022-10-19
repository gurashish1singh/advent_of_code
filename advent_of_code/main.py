from __future__ import annotations

import argparse
from importlib import import_module


def main(argv: list[str] | None = None) -> None:
    package_name = __name__.partition(".")[0]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "year",
        choices=["twenty"],
        help="Advent of Code year",
    )
    parser.add_argument("day", help="Advent of Code day")
    args = parser.parse_args(argv)

    module_name = f"{package_name}.{args.year}.{args.day}"
    mod = import_module(module_name)
    mod.main()


if __name__ == "__main__":
    main()
