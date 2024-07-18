from __future__ import annotations

import pathlib


def solve(input_str: list[str]) -> None:
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


if __name__ == "__main__":
    in_name = "input1.txt"
    curr_dir = pathlib.Path(__file__).parent.resolve()
    input_file = curr_dir / (pathlib.Path("inputs") / pathlib.Path(in_name))
    with open(input_file, "r") as f:
        ans = solve(input_str=f.readlines())
        print(f"Answer for the first problem is: {ans!r}")

    # input_str = """
    # 1abc2
    # pqr3stu8vwx
    # a1b2c3d4e5f
    # treb7uchet
    # """
    # ans = solve(input_str=[l.strip() for l in input_str.split() if l])
    # print(f"Answer for the first problem is: {ans!r}")
