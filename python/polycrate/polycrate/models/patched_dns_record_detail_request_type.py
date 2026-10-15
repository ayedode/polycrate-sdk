from typing import Literal

PatchedDNSRecordDetailRequestType = Literal[
    "A", "AAAA", "ALIAS", "CAA", "CNAME", "HTTPS", "MX", "NAPTR", "NS", "PTR", "SRV", "SSHFP", "SVCB", "TLSA", "TXT"
]

PATCHED_DNS_RECORD_DETAIL_REQUEST_TYPE_VALUES: set[PatchedDNSRecordDetailRequestType] = {
    "A",
    "AAAA",
    "ALIAS",
    "CAA",
    "CNAME",
    "HTTPS",
    "MX",
    "NAPTR",
    "NS",
    "PTR",
    "SRV",
    "SSHFP",
    "SVCB",
    "TLSA",
    "TXT",
}


def check_patched_dns_record_detail_request_type(value: str) -> PatchedDNSRecordDetailRequestType:
    if value in PATCHED_DNS_RECORD_DETAIL_REQUEST_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_DNS_RECORD_DETAIL_REQUEST_TYPE_VALUES!r}")
