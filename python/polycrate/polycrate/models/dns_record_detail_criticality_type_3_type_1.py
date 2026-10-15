from typing import Literal

DNSRecordDetailCriticalityType3Type1 = Literal["", "high", "low", "medium"]

DNS_RECORD_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[DNSRecordDetailCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_dns_record_detail_criticality_type_3_type_1(value: str) -> DNSRecordDetailCriticalityType3Type1:
    if value in DNS_RECORD_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DNS_RECORD_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
