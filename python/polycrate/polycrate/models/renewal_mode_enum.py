from typing import Literal

RenewalModeEnum = Literal["AUTODELETE", "AUTORENEW"]

RENEWAL_MODE_ENUM_VALUES: set[RenewalModeEnum] = {
    "AUTODELETE",
    "AUTORENEW",
}


def check_renewal_mode_enum(value: str) -> RenewalModeEnum:
    if value in RENEWAL_MODE_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RENEWAL_MODE_ENUM_VALUES!r}")
