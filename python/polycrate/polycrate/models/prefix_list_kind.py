from typing import Literal

PrefixListKind = Literal["ipv4", "ipv6"]

PREFIX_LIST_KIND_VALUES: set[PrefixListKind] = {
    "ipv4",
    "ipv6",
}


def check_prefix_list_kind(value: str) -> PrefixListKind:
    if value in PREFIX_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PREFIX_LIST_KIND_VALUES!r}")
