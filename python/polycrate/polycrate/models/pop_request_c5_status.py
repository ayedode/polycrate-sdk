from typing import Literal

PopRequestC5Status = Literal["none", "planned", "typ1", "typ2"]

POP_REQUEST_C5_STATUS_VALUES: set[PopRequestC5Status] = {
    "none",
    "planned",
    "typ1",
    "typ2",
}


def check_pop_request_c5_status(value: str) -> PopRequestC5Status:
    if value in POP_REQUEST_C5_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_REQUEST_C5_STATUS_VALUES!r}")
