from typing import Literal

PopRequestColocation = Literal["no", "planned", "unknown", "yes"]

POP_REQUEST_COLOCATION_VALUES: set[PopRequestColocation] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_pop_request_colocation(value: str) -> PopRequestColocation:
    if value in POP_REQUEST_COLOCATION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_REQUEST_COLOCATION_VALUES!r}")
