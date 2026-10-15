from typing import Literal

PatchedPrefixRequestKind = Literal["ipv4", "ipv6"]

PATCHED_PREFIX_REQUEST_KIND_VALUES: set[PatchedPrefixRequestKind] = {
    "ipv4",
    "ipv6",
}


def check_patched_prefix_request_kind(value: str) -> PatchedPrefixRequestKind:
    if value in PATCHED_PREFIX_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_PREFIX_REQUEST_KIND_VALUES!r}")
