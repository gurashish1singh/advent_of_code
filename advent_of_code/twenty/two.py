from __future__ import annotations

import re

from advent_of_code.common import parse_input
from advent_of_code.twenty.constants import INPUT_STRING_2

PASSWORD_REGEX = r"(?P<ranges>\d{1,2}\-\d{1,2})\s(?P<letter>\w)\:\s(?P<actual_password>[a-z]{1,})"


def main() -> None:
    # sample_input = """
    #     1-3 a: abcde
    #     1-3 b: cdefg
    #     2-9 c: ccccccccc
    # """
    pv = PasswordVerifier(INPUT_STRING_2)

    valid_passwords_one = pv.verify_passwords()
    print(f"{valid_passwords_one = }")

    valid_passwords_two = pv.verify_passwords_with_new_policy()
    print(f"{valid_passwords_two = }")


class PasswordVerifier:
    def __init__(self, input_string: str) -> None:
        self.input_string = input_string
        self.passwords = parse_input(self.input_string)

    def verify_passwords(self) -> int:
        # Assumption here is that the input list will be clean and follow the same pattern,
        # hence I will not do any additional error handling.
        valid_passwords = 0
        for password in self.passwords:
            if matched := re.search(PASSWORD_REGEX, password):
                ranges, letter, actual_password = matched.groups()

            if letter in actual_password:
                min_range, max_range = map(int, ranges.split("-"))
                count = actual_password.count(letter)
                if min_range <= count and max_range >= count:
                    valid_passwords += 1
        return valid_passwords

    def verify_passwords_with_new_policy(self) -> int:
        # Same assumption as above
        valid_passwords = 0
        for password in self.passwords:
            if matched := re.search(PASSWORD_REGEX, password):
                positions, letter, actual_password = matched.groups()

            if letter in actual_password:
                first_position, second_position = map(int, positions.split("-"))
                # According to the problem statement index starts from 1,
                # so i am not going to explicitly check for first_position to be 0
                first_position, second_position = first_position - 1, second_position - 1
                first_position_check = actual_password[first_position] == letter
                second_position_check = actual_password[second_position] == letter
                if first_position_check ^ second_position_check:
                    # According to the problem statement you cannot
                    # have the letter in both positions
                    valid_passwords += 1
        return valid_passwords
