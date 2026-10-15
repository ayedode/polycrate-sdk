from typing import Literal

IPAddressScope = Literal["system", "user"]

IP_ADDRESS_SCOPE_VALUES: set[IPAddressScope] = {
    "system",
    "user",
}


def check_ip_address_scope(value: str) -> IPAddressScope:
    if value in IP_ADDRESS_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IP_ADDRESS_SCOPE_VALUES!r}")
