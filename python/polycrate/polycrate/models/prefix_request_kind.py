from typing import Literal

PrefixRequestKind = Literal["ipv4", "ipv6"]

PREFIX_REQUEST_KIND_VALUES: set[PrefixRequestKind] = {
    "ipv4",
    "ipv6",
}


def check_prefix_request_kind(value: str) -> PrefixRequestKind:
    if value in PREFIX_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PREFIX_REQUEST_KIND_VALUES!r}")
