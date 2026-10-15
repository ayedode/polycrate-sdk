from typing import Literal

IPAddressRequestKind = Literal["ipv4", "ipv6"]

IP_ADDRESS_REQUEST_KIND_VALUES: set[IPAddressRequestKind] = {
    "ipv4",
    "ipv6",
}


def check_ip_address_request_kind(value: str) -> IPAddressRequestKind:
    if value in IP_ADDRESS_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IP_ADDRESS_REQUEST_KIND_VALUES!r}")
