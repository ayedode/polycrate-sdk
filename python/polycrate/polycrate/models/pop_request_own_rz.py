from typing import Literal

PopRequestOwnRz = Literal["no", "planned", "unknown", "yes"]

POP_REQUEST_OWN_RZ_VALUES: set[PopRequestOwnRz] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_pop_request_own_rz(value: str) -> PopRequestOwnRz:
    if value in POP_REQUEST_OWN_RZ_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_REQUEST_OWN_RZ_VALUES!r}")
