from math import prod
from typing import Sequence

from constants import (
    INPUT_LIST,
    TARGET,
)


def three_sum_to_target(target: int, input_args: Sequence[int]) -> tuple[int, ...]:
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
    ret_val = three_sum_to_target(TARGET, INPUT_LIST)
    print(ret_val)
    final_answer = prod(ret_val)
    print(final_answer)
