from typing import Literal

PatchedDNSRecordDetailRequestKind = Literal["generic"]

PATCHED_DNS_RECORD_DETAIL_REQUEST_KIND_VALUES: set[PatchedDNSRecordDetailRequestKind] = {
    "generic",
}


def check_patched_dns_record_detail_request_kind(value: str) -> PatchedDNSRecordDetailRequestKind:
    if value in PATCHED_DNS_RECORD_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_DNS_RECORD_DETAIL_REQUEST_KIND_VALUES!r}")
