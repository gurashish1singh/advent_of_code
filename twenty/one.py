from math import prod

from common import parse_input
from twenty.constants import (
    INPUT_STRING_1,
    TARGET_1,
)


def main():
    # sample_input = [
    #     1721,
    #     366,
    #     299,
    #     675,
    #     979,
    #     1456
    # ]
    erf = ExpenseReportFixer(TARGET_1, INPUT_STRING_1)
    ret_val_one = erf.fix_expense_report()
    print(f"{ret_val_one = }")
    final_answer_one = prod(ret_val_one)
    print(f"{final_answer_one = }")

    ret_val_two = erf.three_sum_to_target()
    print(f"{ret_val_two = }")
    final_answer_two = prod(ret_val_two)
    print(f"{final_answer_two = }")


class ExpenseReportFixer:
    def __init__(self, target: int, input_string: str) -> None:
        self.target = target
        self.input_string = input_string
        self.numbers = list(map(int, parse_input(self.input_string)))

    def fix_expense_report(self) -> int:
        # It's a two-sum problem basically.
        # not going to check for lists with less than 2 items,
        # and the assumption is that the input args will have one unique solution.
        diffs = {}
        for val in self.numbers:
            diff = self.target - val
            if diff in diffs:
                return diff, val
            diffs[val] = diff

    def three_sum_to_target(self) -> tuple[int, ...]:
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
