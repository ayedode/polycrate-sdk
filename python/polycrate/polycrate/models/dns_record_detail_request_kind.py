from typing import Literal

DNSRecordDetailRequestKind = Literal["generic"]

DNS_RECORD_DETAIL_REQUEST_KIND_VALUES: set[DNSRecordDetailRequestKind] = {
    "generic",
}


def check_dns_record_detail_request_kind(value: str) -> DNSRecordDetailRequestKind:
    if value in DNS_RECORD_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNS_RECORD_DETAIL_REQUEST_KIND_VALUES!r}")
