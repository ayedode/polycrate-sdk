from typing import Literal

VersioningStatusEnum = Literal["enabled", "Enabled", "off", "Suspended", "suspended"]

VERSIONING_STATUS_ENUM_VALUES: set[VersioningStatusEnum] = {
    "enabled",
    "Enabled",
    "off",
    "Suspended",
    "suspended",
}


def check_versioning_status_enum(value: str) -> VersioningStatusEnum:
    if value in VERSIONING_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VERSIONING_STATUS_ENUM_VALUES!r}")
