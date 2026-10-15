from typing import Literal

PatchedDNSZoneDetailRequestKind = Literal["external", "internal"]

PATCHED_DNS_ZONE_DETAIL_REQUEST_KIND_VALUES: set[PatchedDNSZoneDetailRequestKind] = {
    "external",
    "internal",
}


def check_patched_dns_zone_detail_request_kind(value: str) -> PatchedDNSZoneDetailRequestKind:
    if value in PATCHED_DNS_ZONE_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_DNS_ZONE_DETAIL_REQUEST_KIND_VALUES!r}")
