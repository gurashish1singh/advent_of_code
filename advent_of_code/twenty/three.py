from math import prod

from advent_of_code.common import parse_input
from advent_of_code.twenty.constants import INPUT_STRING_3


def main():
    # sample_input = """
    #     ..##.......
    #     #...#...#..
    #     .#....#..#.
    #     ..#.#...#.#
    #     .#...##..#.
    #     ..#.##.....
    #     .#.#.#....#
    #     .#........#
    #     #.##...#...
    #     #...##....#
    #     .#..#...#.#
    # """
    t = Teleport(INPUT_STRING_3)

    # 3 down 1 across
    number_of_trees_one = t.get_number_of_trees_traversed(3, 1)
    print(f"{number_of_trees_one = }")

    # 2nd problem
    traversals = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )
    number_of_trees_two = []
    for index_increment_value, paths_rows_to_skip in traversals:
        number_of_trees = t.get_number_of_trees_traversed(index_increment_value, paths_rows_to_skip)
        number_of_trees_two.append(number_of_trees)
    print(f"{prod(number_of_trees_two) = }")


class Teleport:
    def __init__(self, input_string: str) -> None:
        self.input_string = input_string
        self.path_map = parse_input(self.input_string)

    def get_number_of_trees_traversed(self, index_increment_value: int, path_rows_to_skip: int) -> int:
        current_index = 0
        number_of_trees = 0
        filtered_path = self.get_paths_to_traverse(path_rows_to_skip)
        # Skipping the first "path_rows_to_skip" rows as we have to traverse down
        for path in filtered_path:
            current_index += index_increment_value
            if current_index >= len(path):
                # Since we are incrementing the current_index, we need to wrap around and start from the
                # beginning of the row.
                indexes_beyond_limit = current_index - len(path)
                current_index = indexes_beyond_limit

            if path[current_index] == "#":
                number_of_trees += 1
        return number_of_trees

    def get_paths_to_traverse(self, rows_to_skip: int) -> list[str]:
        # Based on the rows_to_skip this method returns a subset of the list
        return self.path_map[rows_to_skip::rows_to_skip]
