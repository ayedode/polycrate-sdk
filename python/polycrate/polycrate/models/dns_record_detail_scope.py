from typing import Literal

DNSRecordDetailScope = Literal["system", "user"]

DNS_RECORD_DETAIL_SCOPE_VALUES: set[DNSRecordDetailScope] = {
    "system",
    "user",
}


def check_dns_record_detail_scope(value: str) -> DNSRecordDetailScope:
    if value in DNS_RECORD_DETAIL_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNS_RECORD_DETAIL_SCOPE_VALUES!r}")
