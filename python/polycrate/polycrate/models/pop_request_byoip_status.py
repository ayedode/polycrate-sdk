from typing import Literal

PopRequestByoipStatus = Literal["no", "planned", "unknown", "yes"]

POP_REQUEST_BYOIP_STATUS_VALUES: set[PopRequestByoipStatus] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_pop_request_byoip_status(value: str) -> PopRequestByoipStatus:
    if value in POP_REQUEST_BYOIP_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_REQUEST_BYOIP_STATUS_VALUES!r}")
