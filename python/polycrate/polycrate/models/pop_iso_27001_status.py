from typing import Literal

PopIso27001Status = Literal["no", "planned", "unknown", "yes"]

POP_ISO_27001_STATUS_VALUES: set[PopIso27001Status] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_pop_iso_27001_status(value: str) -> PopIso27001Status:
    if value in POP_ISO_27001_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_ISO_27001_STATUS_VALUES!r}")
