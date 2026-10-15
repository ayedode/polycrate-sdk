from typing import Literal

DNSRecordDetailKind = Literal["generic"]

DNS_RECORD_DETAIL_KIND_VALUES: set[DNSRecordDetailKind] = {
    "generic",
}


def check_dns_record_detail_kind(value: str) -> DNSRecordDetailKind:
    if value in DNS_RECORD_DETAIL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNS_RECORD_DETAIL_KIND_VALUES!r}")
