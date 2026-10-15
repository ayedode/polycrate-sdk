from typing import Literal

DNSRecordDetailType = Literal[
    "A", "AAAA", "ALIAS", "CAA", "CNAME", "HTTPS", "MX", "NAPTR", "NS", "PTR", "SRV", "SSHFP", "SVCB", "TLSA", "TXT"
]

DNS_RECORD_DETAIL_TYPE_VALUES: set[DNSRecordDetailType] = {
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


def check_dns_record_detail_type(value: str) -> DNSRecordDetailType:
    if value in DNS_RECORD_DETAIL_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNS_RECORD_DETAIL_TYPE_VALUES!r}")
