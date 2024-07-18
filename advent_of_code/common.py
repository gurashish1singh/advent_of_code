from __future__ import annotations

import io
import pstats
from cProfile import Profile
from functools import wraps
from typing import (
    Any,
    Callable,
)


def profile(func: Callable) -> Any:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        pr = Profile()
        pr.enable()
        return_value = func(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = pstats.SortKey.CUMULATIVE
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return return_value

    return wrapper


def parse_input(raw_input_string: str) -> list[str]:
    # To make my life easier, input is stored as raw string and then code converts
    # it into a list of strings. Weird line sapcing is also removed here that occurs
    # during the triple-quoted string formation.
    return [s.strip() for s in raw_input_string.splitlines() if s.strip()]
