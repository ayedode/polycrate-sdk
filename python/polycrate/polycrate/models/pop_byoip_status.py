from typing import Literal

PopByoipStatus = Literal["no", "planned", "unknown", "yes"]

POP_BYOIP_STATUS_VALUES: set[PopByoipStatus] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_pop_byoip_status(value: str) -> PopByoipStatus:
    if value in POP_BYOIP_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_BYOIP_STATUS_VALUES!r}")
