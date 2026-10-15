from typing import Literal

PopC5Status = Literal["none", "planned", "typ1", "typ2"]

POP_C5_STATUS_VALUES: set[PopC5Status] = {
    "none",
    "planned",
    "typ1",
    "typ2",
}


def check_pop_c5_status(value: str) -> PopC5Status:
    if value in POP_C5_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_C5_STATUS_VALUES!r}")
