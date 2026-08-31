from typing import Literal

EnforcementEnum = Literal["optional", "recommended", "required"]

ENFORCEMENT_ENUM_VALUES: set[EnforcementEnum] = {
    "optional",
    "recommended",
    "required",
}


def check_enforcement_enum(value: str) -> EnforcementEnum:
    if value in ENFORCEMENT_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENFORCEMENT_ENUM_VALUES!r}")
