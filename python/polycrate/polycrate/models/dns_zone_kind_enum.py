from typing import Literal

DNSZoneKindEnum = Literal["external", "internal"]

DNS_ZONE_KIND_ENUM_VALUES: set[DNSZoneKindEnum] = {
    "external",
    "internal",
}


def check_dns_zone_kind_enum(value: str) -> DNSZoneKindEnum:
    if value in DNS_ZONE_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNS_ZONE_KIND_ENUM_VALUES!r}")
