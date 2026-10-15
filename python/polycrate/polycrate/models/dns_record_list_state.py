from typing import Literal

DNSRecordListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

DNS_RECORD_LIST_STATE_VALUES: set[DNSRecordListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_dns_record_list_state(value: str) -> DNSRecordListState:
    if value in DNS_RECORD_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNS_RECORD_LIST_STATE_VALUES!r}")
