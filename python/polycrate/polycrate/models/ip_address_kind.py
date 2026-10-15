from typing import Literal

IPAddressKind = Literal["ipv4", "ipv6"]

IP_ADDRESS_KIND_VALUES: set[IPAddressKind] = {
    "ipv4",
    "ipv6",
}


def check_ip_address_kind(value: str) -> IPAddressKind:
    if value in IP_ADDRESS_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IP_ADDRESS_KIND_VALUES!r}")
