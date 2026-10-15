from typing import Literal

DNSZoneListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

DNS_ZONE_LIST_STATE_VALUES: set[DNSZoneListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_dns_zone_list_state(value: str) -> DNSZoneListState:
    if value in DNS_ZONE_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNS_ZONE_LIST_STATE_VALUES!r}")
