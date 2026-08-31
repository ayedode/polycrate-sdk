from typing import Literal

IPFamilyEnum = Literal["ipv4", "ipv6"]

IP_FAMILY_ENUM_VALUES: set[IPFamilyEnum] = {
    "ipv4",
    "ipv6",
}


def check_ip_family_enum(value: str) -> IPFamilyEnum:
    if value in IP_FAMILY_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IP_FAMILY_ENUM_VALUES!r}")
