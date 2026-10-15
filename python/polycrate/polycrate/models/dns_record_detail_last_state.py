from typing import Literal

DNSRecordDetailLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

DNS_RECORD_DETAIL_LAST_STATE_VALUES: set[DNSRecordDetailLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_dns_record_detail_last_state(value: str) -> DNSRecordDetailLastState:
    if value in DNS_RECORD_DETAIL_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNS_RECORD_DETAIL_LAST_STATE_VALUES!r}")
