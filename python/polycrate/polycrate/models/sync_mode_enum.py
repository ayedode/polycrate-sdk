from typing import Literal

SyncModeEnum = Literal["disabled", "full", "pull", "push"]

SYNC_MODE_ENUM_VALUES: set[SyncModeEnum] = {
    "disabled",
    "full",
    "pull",
    "push",
}


def check_sync_mode_enum(value: str) -> SyncModeEnum:
    if value in SYNC_MODE_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SYNC_MODE_ENUM_VALUES!r}")
