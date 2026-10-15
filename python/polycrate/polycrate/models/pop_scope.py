from typing import Literal

PopScope = Literal["system", "user"]

POP_SCOPE_VALUES: set[PopScope] = {
    "system",
    "user",
}


def check_pop_scope(value: str) -> PopScope:
    if value in POP_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_SCOPE_VALUES!r}")
