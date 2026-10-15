from typing import Literal

PopRequestIso27001Status = Literal["no", "planned", "unknown", "yes"]

POP_REQUEST_ISO_27001_STATUS_VALUES: set[PopRequestIso27001Status] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_pop_request_iso_27001_status(value: str) -> PopRequestIso27001Status:
    if value in POP_REQUEST_ISO_27001_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_REQUEST_ISO_27001_STATUS_VALUES!r}")
