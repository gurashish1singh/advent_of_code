from math import prod

from constants import (
    INPUT_LIST_1,
    TARGET_1,
)


def fix_expense_report(target: int, input_args: list[int]) -> int:
    # It's a two-sum problem basically.
    # not going to check for lists with less than 2 items,
    # and the assumption is that the input args will have one unique solution.
    diffs = {}
    for val in input_args:
        diff = target - val
        if diff in diffs:
            return diff, val
        diffs[val] = diff


def three_sum_to_target(target: int, input_args: list[int]) -> tuple[int, ...]:
    # brute force logic, not at all optimized.
    # not going to check for lists with less than 3 items,
    # and the assumption is that the input args will have one unique solution.
    length = len(input_args)
    for i in range(length - 1):
        val_one = input_args[i]
        diffs = set()
        for j in range(i + 1, length):
            val_two = input_args[j]
            diff = target - val_one - val_two
            if diff in diffs:
                return diff, val_one, val_two
            diffs.add(val_two)


if __name__ == "__main__":
    # il = [
    #     1721,
    #     366,
    #     299,
    #     675,
    #     979,
    #     1456
    # ]
    ret_val_one = fix_expense_report(TARGET_1, INPUT_LIST_1)
    print(f"{ret_val_one = }")
    final_answer_one = prod(ret_val_one)
    print(f"{final_answer_one = }")

    ret_val_two = three_sum_to_target(TARGET_1, INPUT_LIST_1)
    print(f"{ret_val_two = }")
    final_answer_two = prod(ret_val_two)
    print(f"{final_answer_two = }")
