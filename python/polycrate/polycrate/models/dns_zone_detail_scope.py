from typing import Literal

DNSZoneDetailScope = Literal["system", "user"]

DNS_ZONE_DETAIL_SCOPE_VALUES: set[DNSZoneDetailScope] = {
    "system",
    "user",
}


def check_dns_zone_detail_scope(value: str) -> DNSZoneDetailScope:
    if value in DNS_ZONE_DETAIL_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNS_ZONE_DETAIL_SCOPE_VALUES!r}")
