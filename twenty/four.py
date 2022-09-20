import re

from twenty.constants import INPUT_STRING_4


def main():
    # sample_input = """
    # ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    # byr:1937 iyr:2017 cid:147 hgt:183cm

    # iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    # hcl:#cfa07d byr:1929

    # hcl:#ae17e1 iyr:2013
    # eyr:2024
    # ecl:brn pid:760753108 byr:1931
    # hgt:179cm

    # hcl:#cfa07d eyr:2025 pid:166559648
    # iyr:2011 ecl:brn hgt:59in
    # """
    pv = PassportValidator(INPUT_STRING_4)

    valid_passports_one = pv.validate_passports()
    print(f"{len(valid_passports_one) = }")

    valid_passports_two = pv.validate_passports_with_value_validation(valid_passports_one)
    print(f"{valid_passports_two = }")


class PassportValidator:

    # ?= -> negative lookahead, repeat the pattern to find all occurances in a string
    # The first part (before the :) looks for the key and the rest is for values.
    # They can be all strings, or digits, or a combo. "#" is added optional to capture hex values.
    KEY_AND_VALUE_PATTERN = r"(?=(\w{3}):(\#?\w+|\d+|\#?\w+\d+|\#?\d+\w+)\s*?)"
    MANDATORY_FIELDS_VALIDATION = {
        "byr": r"192[0-9]|19[3-9][0-9]|200[0-2]",  # Birth Year, between 1920 and 2002
        "iyr": r"201[0-9]|2020",  # Issue Year, between 2010 and 2020
        "eyr": r"202[0-9]|2030",  # Expiration Year, between 2020 and 2030
        "hgt": r"((15[0-9]|1[6-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in)",  # Height, 150-193cm or 59-76in
        "hcl": r"^#([0-9a-f]{6})",  # Hair Color, #6 characters [0-9] and/or [a-f]
        "ecl": r"amb|blu|brn|gry|grn|hzl|oth",  # Eye Color
        "pid": r"[0-9]{9}$",  # Passport ID
        # "cid",  # Country ID --> Not mandatory
    }
    MANDATORY_KEYS = set(MANDATORY_FIELDS_VALIDATION.keys())

    def __init__(self, input_string: str) -> None:
        self.input_string = input_string
        self.raw_passports = self.parse_input()

    def parse_input(self) -> list[str]:
        # Each new passport is separated by a line break, but the fields in a single
        # passport may also be separated by line break (see sample input). This method cleans up the input
        # and returns a list of strings so that each item in the list is a distinct passport.
        raw_passports = self.input_string.split("\n\n")
        return [line.replace("\n", " ") for line in raw_passports]

    def validate_passports(self) -> list[list[tuple[str, str]]]:
        # Problem 1: Just validate keys
        valid_passports = []
        for line in self.raw_passports:
            passport_fields = re.findall(self.KEY_AND_VALUE_PATTERN, line)
            passport_keys, _ = zip(*passport_fields)
            if self.validate_passport_keys(set(passport_keys)):
                valid_passports.append(passport_fields)
        return valid_passports

    def validate_passports_with_value_validation(self,
                                                 passports_with_valid_keys: list[list[tuple[str, str]]]) -> int:
        # Problem 2: Apart from the keys, values have to be validated as well
        valid_passports = 0
        for passport in passports_with_valid_keys:
            for key, value in passport:
                # Since "cid" is optional, we can skip it
                if key != "cid":
                    pattern_to_compare = self.MANDATORY_FIELDS_VALIDATION[key]
                    if not re.match(pattern_to_compare, value):
                        break
            else:
                valid_passports += 1
        return valid_passports

    def validate_passport_keys(self, passport_keys: set[str]) -> bool:
        if not self.MANDATORY_KEYS.difference(passport_keys):
            return True
        return False
