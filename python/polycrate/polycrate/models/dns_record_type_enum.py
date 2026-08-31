from typing import Literal

DNSRecordTypeEnum = Literal[
    "A", "AAAA", "ALIAS", "CAA", "CNAME", "HTTPS", "MX", "NAPTR", "NS", "PTR", "SRV", "SSHFP", "SVCB", "TLSA", "TXT"
]

DNS_RECORD_TYPE_ENUM_VALUES: set[DNSRecordTypeEnum] = {
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


def check_dns_record_type_enum(value: str) -> DNSRecordTypeEnum:
    if value in DNS_RECORD_TYPE_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNS_RECORD_TYPE_ENUM_VALUES!r}")
