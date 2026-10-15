from typing import Literal

PrefixKind = Literal["ipv4", "ipv6"]

PREFIX_KIND_VALUES: set[PrefixKind] = {
    "ipv4",
    "ipv6",
}


def check_prefix_kind(value: str) -> PrefixKind:
    if value in PREFIX_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PREFIX_KIND_VALUES!r}")
