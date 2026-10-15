from typing import Literal

IPAddressListKind = Literal["ipv4", "ipv6"]

IP_ADDRESS_LIST_KIND_VALUES: set[IPAddressListKind] = {
    "ipv4",
    "ipv6",
}


def check_ip_address_list_kind(value: str) -> IPAddressListKind:
    if value in IP_ADDRESS_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IP_ADDRESS_LIST_KIND_VALUES!r}")
