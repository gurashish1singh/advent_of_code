from __future__ import annotations

import pathlib
import re
from collections import defaultdict
from math import prod

ALLOWED_CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
COLORS = "|".join(ALLOWED_CUBES.keys())
CUBE_PATTERN = rf"(?P<digit>\d+)\s(?P<color>({COLORS}))"
GAME_ID_PATTERN = r"^Game\s(?P<game_id>\d+):"


def solve_one(input_str: str) -> int:
    """
    We have to find out the sum of ids of games that would have been possible to play
    based on the number of allowed cubes in ALLOWED_CUBES constant.
    """
    game_ids = []
    for line in input_str:
        color_to_num_dict = defaultdict(int)
        game_possible = True
        # Extract the id first
        game_id = int(re.match(GAME_ID_PATTERN, line).groups()[0])
        # Total number of sets revealed are separated by ;
        cleaned_line = line.split(":")[-1].split(";")

        for games in cleaned_line:
            games = games.strip()
            # Each reveal is split by ,
            for game in games.split(","):
                match = re.match(CUBE_PATTERN, game.strip()).groupdict()
                num = int(match["digit"])
                color = match["color"]
                color_to_num_dict[color] += num
                # Short-circuit early if the number of cubes are greater than allowed
                if ALLOWED_CUBES.get(color) < num:
                    game_possible = False
                    break

        # Only append if the game is allowed
        if game_possible:
            game_ids.append(game_id)
    return sum(game_ids)


def solve_two(input_str: str) -> int:
    """
    For a given set of reveals, we need to find out the minimum number of cubes required per color
    to make a game possible. Return sum of power of cubes.
    power of cubes = (max number of individual colors per reveal multiplied together)
    """
    all_power_of_cubes = []
    for line in input_str:
        color_to_num_dict = {}
        # Total number of sets revealed are separated by ;
        cleaned_line = line.split(":")[-1].split(";")

        for games in cleaned_line:
            games = games.strip()
            # Each reveal is split by ,
            for game in games.split(","):
                match = re.match(CUBE_PATTERN, game.strip()).groupdict()
                num = int(match["digit"])
                color = match["color"]
                # We add the highest value of the color seen so far
                if color in color_to_num_dict:
                    color_to_num_dict[color] = max(num, color_to_num_dict[color])
                else:
                    color_to_num_dict[color] = num

        power_of_cubes = prod(color_to_num_dict.values())
        all_power_of_cubes.append(power_of_cubes)
    return sum(all_power_of_cubes)


if __name__ == "__main__":
    # Part one
    # Test input
    input_str_1 = """
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    """
    ans = solve_one(input_str=[line.strip() for line in input_str_1.split("\n") if line.strip()])
    print(f"Answer for the first problem of Day 2 is: {ans!r}")
    assert ans == 8, f"{ans!r} is not correct."

    # Actual input
    in_name = "input2.txt"
    curr_dir = pathlib.Path(__file__).parent.resolve()
    input_file = curr_dir / (pathlib.Path("inputs") / pathlib.Path(in_name))
    with open(input_file, "r") as f:
        ans = solve_one(input_str=f.readlines())
        print(f"Answer for the first problem of Day 2 is: {ans!r}")

    # Part Two
    # Test input
    input_str_2 = """
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    """
    ans = solve_two(input_str=[line.strip() for line in input_str_2.split("\n") if line.strip()])
    print(f"Answer for the second problem of Day 2 is: {ans!r}")
    assert ans == 2286, f"{ans!r} is not correct."

    # Actual input
    with open(input_file, "r") as f:
        ans = solve_two(input_str=f.readlines())
        print(f"Answer for the first problem of Day 2 is: {ans!r}")
