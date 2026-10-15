from typing import Literal

PatchedIPAddressRequestKind = Literal["ipv4", "ipv6"]

PATCHED_IP_ADDRESS_REQUEST_KIND_VALUES: set[PatchedIPAddressRequestKind] = {
    "ipv4",
    "ipv6",
}


def check_patched_ip_address_request_kind(value: str) -> PatchedIPAddressRequestKind:
    if value in PATCHED_IP_ADDRESS_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_IP_ADDRESS_REQUEST_KIND_VALUES!r}")
