from typing import Literal

DNSZoneDetailState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

DNS_ZONE_DETAIL_STATE_VALUES: set[DNSZoneDetailState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_dns_zone_detail_state(value: str) -> DNSZoneDetailState:
    if value in DNS_ZONE_DETAIL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNS_ZONE_DETAIL_STATE_VALUES!r}")
