from typing import Literal

PrefixListPurpose = Literal["controlplane", "loadbalancer"]

PREFIX_LIST_PURPOSE_VALUES: set[PrefixListPurpose] = {
    "controlplane",
    "loadbalancer",
}


def check_prefix_list_purpose(value: str) -> PrefixListPurpose:
    if value in PREFIX_LIST_PURPOSE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PREFIX_LIST_PURPOSE_VALUES!r}")
