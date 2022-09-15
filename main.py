import argparse
from importlib import import_module
from typing import Optional


YEAR_TO_MODULE_NAME_MAP = {
    "2020": "twenty"
}


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "year",
        choices=["2020"],
        help="Advent of Code year",
    )
    parser.add_argument(
        "day",
        help="Advent of Code day"
    )
    args = parser.parse_args(argv)

    name = f"{YEAR_TO_MODULE_NAME_MAP[args.year]}.{args.day}"
    mod = import_module(name)
    mod.main()


if __name__ == "__main__":
    main()
