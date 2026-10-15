from typing import Literal

DNSZoneDetailLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

DNS_ZONE_DETAIL_LAST_STATE_VALUES: set[DNSZoneDetailLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_dns_zone_detail_last_state(value: str) -> DNSZoneDetailLastState:
    if value in DNS_ZONE_DETAIL_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNS_ZONE_DETAIL_LAST_STATE_VALUES!r}")
