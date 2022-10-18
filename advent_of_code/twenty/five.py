from common import parse_input
from twenty.constants import INPUT_STRING_5


def main():
    # il = """
    #     FBFBBFFRLR
    #     BFFFBBFRRR
    #     FFFBBBFRRR
    #     BBFFBBFRLL
    # """
    sf = SeatFinder(INPUT_STRING_5)
    sf.find_seat()
    valid_seats, invalid_seats = sf.valids, sf.invalids
    if invalid_seats:
        print(f"Found some invalid seat string:\n{invalid_seats = }")
    highest_seat_id = max(valid_seats)
    print(f"{highest_seat_id = }")


class SeatFinder:

    COLUMNS = list(range(8))
    ROWS = list(range(128))
    VALID_STRING_LENGTH = 10

    def __init__(self, input_string: str) -> None:
        self.input_string = input_string
        self.invalids: list[str] = []
        self.seat_numbers = parse_input(self.input_string)
        self.valids: list[str] = []

    def find_seat(self) -> None:
        for seat in self.seat_numbers:
            first_seven = seat[:7]
            last_three = seat[7:]
            if self.validate_string(seat, first_seven, last_three):
                row_number = self.traverse_rows(first_seven)
                column_number = self.traverse_columns(last_three)
                self.valids.append(
                    self.unique_seat_id(row_number, column_number)
                )

    def validate_string(self, seat: str, first_seven: str, last_three: str) -> bool:
        if len(seat) != self.VALID_STRING_LENGTH:
            self.invalids.append(seat)
            return False

        if "F" not in first_seven and "B" not in first_seven:
            self.invalids.append(seat)
            return False
        elif "R" not in last_three and "L" not in last_three:
            self.invalids.append(seat)
            return False
        return True

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
