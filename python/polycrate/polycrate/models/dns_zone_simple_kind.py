from typing import Literal

DNSZoneSimpleKind = Literal["external", "internal"]

DNS_ZONE_SIMPLE_KIND_VALUES: set[DNSZoneSimpleKind] = {
    "external",
    "internal",
}


def check_dns_zone_simple_kind(value: str) -> DNSZoneSimpleKind:
    if value in DNS_ZONE_SIMPLE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNS_ZONE_SIMPLE_KIND_VALUES!r}")
