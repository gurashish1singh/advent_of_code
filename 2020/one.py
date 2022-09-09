from math import prod
from typing import Sequence

from constants import (
    INPUT_LIST,
    TARGET,
)


def fix_expense_report(target: int, input_args: Sequence[int]) -> int:
    # It's a two-sum problem basically.
    # not going to check for lists with less than 2 items,
    # and the assumption is that the input args will have one unique solution.
    diffs = {}
    for val in input_args:
        diff = target - val
        if diff in diffs:
            return diff, val
        diffs[val] = diff


if __name__ == "__main__":
    ret_val = fix_expense_report(TARGET, INPUT_LIST)
    print(ret_val)
    final_answer = prod(ret_val)
    print(final_answer)
