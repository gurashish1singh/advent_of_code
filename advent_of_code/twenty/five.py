from __future__ import annotations

from advent_of_code.common import parse_input
from advent_of_code.twenty.constants import INPUT_STRING_5


def main():
    # il = """
    #     FBFBBFFRLR
    #     BFFFBBFRRR
    #     FFFBBBFRRR
    #     BBFFBBFRLL
    # """
    sf = SeatFinder(INPUT_STRING_5)
    sf.part_one()
    sf.part_two()


class SeatFinder:

    COLUMNS = list(range(8))
    ROWS = list(range(128))

    def __init__(self, input_string: str) -> None:
        self.seat_numbers: list[str] = parse_input(input_string)
        self.seats: list[int] = []

    def part_one(self):
        self.find_seat()
        # self.find_seat_more_efficiently()
        highest_seat_id = max(self.seats)
        print(f"{highest_seat_id = }")

    def part_two(self):
        ...

    def find_seat(self) -> None:
        for seat in self.seat_numbers:
            first_seven = seat[:7]
            last_three = seat[7:]
            row_number = self.traverse_rows(first_seven)
            column_number = self.traverse_columns(last_three)
            self.seats.append(self.unique_seat_id(row_number, column_number))

    def traverse_rows(self, seat: str) -> int:
        rows_left_to_search = self.ROWS
        for char in seat:
            row_splitter = len(rows_left_to_search) // 2
            if char == "F":
                rows_left_to_search = rows_left_to_search[:row_splitter]
            elif char == "B":
                rows_left_to_search = rows_left_to_search[row_splitter:]
        return rows_left_to_search[-1]

    def traverse_columns(self, seat: str) -> int:
        columns_left_to_search = self.COLUMNS
        for char in seat:
            column_splitter = len(columns_left_to_search) // 2
            if char == "L":
                columns_left_to_search = columns_left_to_search[:column_splitter]
            elif char == "R":
                columns_left_to_search = columns_left_to_search[column_splitter:]
        return columns_left_to_search[-1]

    def unique_seat_id(self, row_number: int, column_number: int) -> int:
        return (row_number * 8) + column_number

    def find_seat_more_efficiently(self) -> None:
        # This one is done through bit magic.
        # Kudos @anthonywritescode for this solution.
        for seat in self.seat_numbers:
            seat = seat.replace("F", "0").replace("B", "1")
            seat = seat.replace("L", "0").replace("R", "1")
            # Converting to base 2
            self.seats.append(int(seat, base=2))
