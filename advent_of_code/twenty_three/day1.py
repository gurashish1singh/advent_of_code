from __future__ import annotations

import pathlib

SPELLED_OUT_DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def solve_one(input_str: list[str]) -> None:
    """
    Each line contains atleast one digit. We need to select the 1st and the last digit
    while traversing through the string. Combine both digits to form a two digit number.
    Final output is the sum of all such two digit numbers.
    """
    nums = []
    for line in input_str:
        line = line.strip()
        left_idx = 0
        length = len(line)
        right_idx = length - 1
        first_num = None

        while left_idx <= (length - 1):
            left_char = line[left_idx]
            if left_char.isdigit():
                first_num = left_char
                break
            left_idx += 1

        # Short-circuit
        if first_num is None:
            nums.append(0)
            break

        while right_idx >= 0:
            right_char = line[right_idx]
            if right_char.isdigit():
                last_num = right_char
                break
            right_idx -= 1

        nums.append(int(f"{first_num}{last_num}"))
    return sum(nums)


def solve_two(input_str: list[str]) -> int:
    """
    Continuation from the previous problem, a line could consist of a spelled out digit.
    """
    nums = []
    for line in input_str:
        line = line.strip()
        left_idx = 0
        length = len(line)
        right_idx = length - 1
        first_num = None

        while left_idx < length:
            char = line[left_idx]
            # We shift the word one digit to the right so tha we can
            # check if it matches any of the word in SPELLED_OUT_DIGITS
            word = line[left_idx:]
            # Check if its an actual digit
            if char.isdigit():
                first_num = char
                break

            # Next we'll check if the shifted word startswith any of the spelled out digits
            if any(word.startswith(word_digit) for word_digit in SPELLED_OUT_DIGITS):
                first_num = _get_spelled_out_digit(word=word, start=True)
                break

            # If neither of the above conditions are met, we increment
            left_idx += 1

        # Short-circuit in case first_num is not found
        if first_num is None:
            break

        while right_idx >= 0:
            char = line[right_idx]
            # We shift the word one digit to the left so tha we can
            # check if it endswith any of the word in SPELLED_OUT_DIGITS
            word = line[: right_idx + 1]

            # Similar to the previous block, we first check if the char is a digit
            if char.isdigit():
                last_num = char
                break

            # Next we check if the shifted word endswith any of the spelled out digits
            if any(word.endswith(word_digit) for word_digit in SPELLED_OUT_DIGITS):
                last_num = _get_spelled_out_digit(word=word, start=False)
                break

            # If neither of the above conditions are met, we decrement
            right_idx -= 1

        nums.append(int(f"{first_num}{last_num}"))
    return sum(nums)


def _get_spelled_out_digit(word: str, start: bool) -> str:
    func = str.startswith if start else str.endswith
    for spelled_out_digit, digit in SPELLED_OUT_DIGITS.items():
        if func(word, spelled_out_digit):
            return digit


if __name__ == "__main__":
    # Test input 1
    input_str_1 = """
    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    """
    ans = solve_one(input_str=[line.strip() for line in input_str_1.split() if line])
    print(f"Answer for the first problem of Day 1 is: {ans!r}")
    assert ans == 142

    # Actual input
    in_name = "input1.txt"
    curr_dir = pathlib.Path(__file__).parent.resolve()
    input_file = curr_dir / (pathlib.Path("inputs") / pathlib.Path(in_name))
    with open(input_file, "r") as f:
        ans = solve_one(input_str=f.readlines())
        print(f"Answer for the first problem of Day 1 is: {ans!r}")

    # Test input 2
    input_str_2 = """
    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen
    """
    ans = solve_two(input_str=[line.strip() for line in input_str_2.split() if line])
    print(f"Answer for the second problem of Day 1 is: {ans!r}")
    assert ans == 281, f"{ans!r} is not correct."

    # Actual input
    with open(input_file, "r") as f:
        ans = solve_two(input_str=f.readlines())
        print(f"Answer for the second problem of Day 1 is: {ans!r}")
