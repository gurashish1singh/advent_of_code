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

    valid_passports = pv.validate_passport()
    print(valid_passports)


class PassportValidator:

    MANDATORY_FIELDS = {
        "byr",  # Birth Year
        "iyr",  # Issue Year
        "eyr",  # Expiration Year
        "hgt",  # Height
        "hcl",  # Hair Color
        "ecl",  # Eye Color
        "pid",  # Passport ID
        # "cid",  # Country ID --> Not mandatory
    }

    def __init__(self, input_string: str) -> None:
        self.input_string = input_string

    def validate_passport(self) -> int:
        valid_passport_pattern = r"(\w{3}):"
        valid_passports = 0
        passport_fields = set()
        for line in self.input_string.splitlines():
            line = line.strip()
            # Filtering out whitespace and new lines.
            if line:
                # Extract the passport fields from the string.
                matched_line = re.findall(valid_passport_pattern, line)
                passport_fields.update(matched_line)
            else:
                # For new lines and whitepace we reset the container.
                # Each distinct passport will be separated by new line.
                passport_fields = set()
            if not self.MANDATORY_FIELDS.difference(passport_fields):
                valid_passports += 1
        return valid_passports
