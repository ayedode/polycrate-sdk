from typing import Literal

PurposeFf5Enum = Literal["controlplane", "loadbalancer"]

PURPOSE_FF_5_ENUM_VALUES: set[PurposeFf5Enum] = {
    "controlplane",
    "loadbalancer",
}


def check_purpose_ff_5_enum(value: str) -> PurposeFf5Enum:
    if value in PURPOSE_FF_5_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PURPOSE_FF_5_ENUM_VALUES!r}")
