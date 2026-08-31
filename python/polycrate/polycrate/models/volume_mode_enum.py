from typing import Literal

VolumeModeEnum = Literal["Block", "Filesystem"]

VOLUME_MODE_ENUM_VALUES: set[VolumeModeEnum] = {
    "Block",
    "Filesystem",
}


def check_volume_mode_enum(value: str) -> VolumeModeEnum:
    if value in VOLUME_MODE_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VOLUME_MODE_ENUM_VALUES!r}")
