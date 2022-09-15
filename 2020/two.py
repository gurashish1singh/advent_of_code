import re
from collections import Counter

from constants import INPUT_LIST_2


PASSWORD_REGEX = r"(?P<ranges>\d{1,2}\-\d{1,2})\s(?P<letter>\w)\:\s(?P<actual_password>[a-z]{1,})"


def verify_passwords(input_list: list[str]) -> int:
    # Assumption here is that the input list will be clean and follow the same pattern,
    # hence I will not do any additional error handling.
    valid_passwords = 0
    for password in input_list:
        ranges, letter, actual_password = re.search(PASSWORD_REGEX, password).groups()
        if letter in actual_password:
            min_range, max_range = map(int, ranges.split("-"))
            c = Counter(actual_password)
            count = c.get(letter)
            if min_range <= count and max_range >= count:
                valid_passwords += 1
    return valid_passwords


def verify_passwords_with_new_policy(input_list: list[str]) -> int:
    # Same assumption as above
    valid_passwords = 0
    for password in input_list:
        positions, letter, actual_password = re.search(PASSWORD_REGEX, password).groups()
        if letter in actual_password:
            first_position, second_position = map(int, positions.split("-"))
            # According to the problem statement index starts from 1, so i am not going to explicitly
            # check for first_position to be 0
            first_position, second_position = first_position - 1, second_position - 1
            if actual_password[first_position] == letter and actual_password[second_position] == letter:
                # Only one of the given positions are valid
                continue
            elif actual_password[first_position] == letter or actual_password[second_position] == letter:
                valid_passwords += 1
    return valid_passwords


if __name__ == "__main__":
    il = [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc"
    ]
    valid_passwords_one = verify_passwords(INPUT_LIST_2)
    print(f"{valid_passwords_one = }")

    valid_passwords_two = verify_passwords_with_new_policy(INPUT_LIST_2)
    print(f"{valid_passwords_two = }")
