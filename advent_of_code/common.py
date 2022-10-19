def parse_input(raw_input_string: str) -> list[str]:
    # To make my life easier, input is stored as raw string and then code converts
    # it into a list of strings. Weird line sapcing is also removed here that occurs
    # during the triple-quoted string formation.
    return [s.strip() for s in raw_input_string.splitlines() if s.strip()]
