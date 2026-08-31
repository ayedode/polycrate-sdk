from typing import Literal

Status18BEnum = Literal["accepted", "false_positive", "fixed", "open", "wont_fix"]

STATUS_18B_ENUM_VALUES: set[Status18BEnum] = {
    "accepted",
    "false_positive",
    "fixed",
    "open",
    "wont_fix",
}


def check_status_18b_enum(value: str) -> Status18BEnum:
    if value in STATUS_18B_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_18B_ENUM_VALUES!r}")
