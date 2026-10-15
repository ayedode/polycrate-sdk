from typing import Literal

PopColocation = Literal["no", "planned", "unknown", "yes"]

POP_COLOCATION_VALUES: set[PopColocation] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_pop_colocation(value: str) -> PopColocation:
    if value in POP_COLOCATION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_COLOCATION_VALUES!r}")
