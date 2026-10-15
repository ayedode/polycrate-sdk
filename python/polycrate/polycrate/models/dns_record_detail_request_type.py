from typing import Literal

DNSRecordDetailRequestType = Literal[
    "A", "AAAA", "ALIAS", "CAA", "CNAME", "HTTPS", "MX", "NAPTR", "NS", "PTR", "SRV", "SSHFP", "SVCB", "TLSA", "TXT"
]

DNS_RECORD_DETAIL_REQUEST_TYPE_VALUES: set[DNSRecordDetailRequestType] = {
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


def check_dns_record_detail_request_type(value: str) -> DNSRecordDetailRequestType:
    if value in DNS_RECORD_DETAIL_REQUEST_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNS_RECORD_DETAIL_REQUEST_TYPE_VALUES!r}")
