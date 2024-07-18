from __future__ import annotations

from math import prod

from advent_of_code.common import parse_input
from advent_of_code.twenty.constants import (
    INPUT_STRING_1,
    TARGET_1,
)


def main():
    erf = ExpenseReportFixer(TARGET_1, INPUT_STRING_1)
    ret_val_one = erf.fix_expense_report()
    print(f"{ret_val_one = }")
    final_answer_one = erf.final_product(ret_val_one)
    print(f"{final_answer_one = }")

    ret_val_two = erf.three_sum_to_target()
    print(f"{ret_val_two = }")
    final_answer_two = erf.final_product(ret_val_two)
    print(f"{final_answer_two = }")


class ExpenseReportFixer:
    def __init__(self, target: int, input_string: str) -> None:
        self.target = target
        self.input_string = input_string
        self.numbers = list(map(int, parse_input(self.input_string)))

    def fix_expense_report(self) -> tuple[int, int]:
        # It's a two-sum problem basically.
        # not going to check for lists with less than 2 items,
        # and the assumption is that the input args will have one unique solution.
        diffs = {}
        for val in self.numbers:
            diff = self.target - val
            if diff in diffs:
                return diff, val
            diffs[val] = diff
        raise ValueError(f"No solution found for target: {self.target} in {self.numbers}")

    def three_sum_to_target(self) -> tuple[int, int, int]:
        # brute force logic, not at all optimized.
        # not going to check for lists with less than 3 items,
        # and the assumption is that the input args will have one unique solution.
        length = len(self.numbers)
        for i in range(length - 1):
            val_one = self.numbers[i]
            diffs = set()
            for j in range(i + 1, length):
                val_two = self.numbers[j]
                diff = self.target - val_one - val_two
                if diff in diffs:
                    return diff, val_one, val_two
                diffs.add(val_two)
        raise ValueError(f"No solution found for target: {self.target} in {self.numbers}")

    def final_product(self, tuple_values: tuple[int, ...]) -> int:
        return prod(tuple_values)
