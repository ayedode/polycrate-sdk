from typing import Literal

PrefixPurpose = Literal["controlplane", "loadbalancer"]

PREFIX_PURPOSE_VALUES: set[PrefixPurpose] = {
    "controlplane",
    "loadbalancer",
}


def check_prefix_purpose(value: str) -> PrefixPurpose:
    if value in PREFIX_PURPOSE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PREFIX_PURPOSE_VALUES!r}")
