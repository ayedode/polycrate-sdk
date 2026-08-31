from typing import Literal

PhaseEnum = Literal["Available", "Bound", "Failed", "Pending", "Released", "Unknown"]

PHASE_ENUM_VALUES: set[PhaseEnum] = {
    "Available",
    "Bound",
    "Failed",
    "Pending",
    "Released",
    "Unknown",
}


def check_phase_enum(value: str) -> PhaseEnum:
    if value in PHASE_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PHASE_ENUM_VALUES!r}")
