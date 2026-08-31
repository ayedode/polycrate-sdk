from typing import Literal

PurposeF3BEnum = Literal["development", "infrastructure", "platform", "production", "qa", "staging"]

PURPOSE_F3B_ENUM_VALUES: set[PurposeF3BEnum] = {
    "development",
    "infrastructure",
    "platform",
    "production",
    "qa",
    "staging",
}


def check_purpose_f3b_enum(value: str) -> PurposeF3BEnum:
    if value in PURPOSE_F3B_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PURPOSE_F3B_ENUM_VALUES!r}")
