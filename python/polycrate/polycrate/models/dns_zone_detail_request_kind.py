from typing import Literal

DNSZoneDetailRequestKind = Literal["external", "internal"]

DNS_ZONE_DETAIL_REQUEST_KIND_VALUES: set[DNSZoneDetailRequestKind] = {
    "external",
    "internal",
}


def check_dns_zone_detail_request_kind(value: str) -> DNSZoneDetailRequestKind:
    if value in DNS_ZONE_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNS_ZONE_DETAIL_REQUEST_KIND_VALUES!r}")
