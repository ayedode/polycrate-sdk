from typing import Literal

StatusA85Enum = Literal["disputed", "open", "rejected", "reserved"]

STATUS_A85_ENUM_VALUES: set[StatusA85Enum] = {
    "disputed",
    "open",
    "rejected",
    "reserved",
}


def check_status_a85_enum(value: str) -> StatusA85Enum:
    if value in STATUS_A85_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_A85_ENUM_VALUES!r}")
