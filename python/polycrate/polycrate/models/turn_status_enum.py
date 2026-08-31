from typing import Literal

TurnStatusEnum = Literal["idle", "queued", "running"]

TURN_STATUS_ENUM_VALUES: set[TurnStatusEnum] = {
    "idle",
    "queued",
    "running",
}


def check_turn_status_enum(value: str) -> TurnStatusEnum:
    if value in TURN_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TURN_STATUS_ENUM_VALUES!r}")
