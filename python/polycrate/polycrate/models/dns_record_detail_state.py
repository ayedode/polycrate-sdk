from typing import Literal

DNSRecordDetailState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

DNS_RECORD_DETAIL_STATE_VALUES: set[DNSRecordDetailState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_dns_record_detail_state(value: str) -> DNSRecordDetailState:
    if value in DNS_RECORD_DETAIL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNS_RECORD_DETAIL_STATE_VALUES!r}")
