from typing import Literal

DNSZoneDetailKind = Literal["external", "internal"]

DNS_ZONE_DETAIL_KIND_VALUES: set[DNSZoneDetailKind] = {
    "external",
    "internal",
}


def check_dns_zone_detail_kind(value: str) -> DNSZoneDetailKind:
    if value in DNS_ZONE_DETAIL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNS_ZONE_DETAIL_KIND_VALUES!r}")
