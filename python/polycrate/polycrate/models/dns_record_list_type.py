from typing import Literal

DNSRecordListType = Literal[
    "A", "AAAA", "ALIAS", "CAA", "CNAME", "HTTPS", "MX", "NAPTR", "NS", "PTR", "SRV", "SSHFP", "SVCB", "TLSA", "TXT"
]

DNS_RECORD_LIST_TYPE_VALUES: set[DNSRecordListType] = {
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


def check_dns_record_list_type(value: str) -> DNSRecordListType:
    if value in DNS_RECORD_LIST_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNS_RECORD_LIST_TYPE_VALUES!r}")
