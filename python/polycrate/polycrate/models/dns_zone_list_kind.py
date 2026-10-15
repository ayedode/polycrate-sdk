from typing import Literal

DNSZoneListKind = Literal["external", "internal"]

DNS_ZONE_LIST_KIND_VALUES: set[DNSZoneListKind] = {
    "external",
    "internal",
}


def check_dns_zone_list_kind(value: str) -> DNSZoneListKind:
    if value in DNS_ZONE_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNS_ZONE_LIST_KIND_VALUES!r}")
