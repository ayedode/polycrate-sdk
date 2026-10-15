from typing import Literal

DNSRecordDetailCriticalityType1 = Literal["", "high", "low", "medium"]

DNS_RECORD_DETAIL_CRITICALITY_TYPE_1_VALUES: set[DNSRecordDetailCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_dns_record_detail_criticality_type_1(value: str) -> DNSRecordDetailCriticalityType1:
    if value in DNS_RECORD_DETAIL_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNS_RECORD_DETAIL_CRITICALITY_TYPE_1_VALUES!r}")
