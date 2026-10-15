from typing import Literal

DNSRecordDetailEffectiveCriticalityType1 = Literal["high", "low", "medium"]

DNS_RECORD_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[DNSRecordDetailEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_dns_record_detail_effective_criticality_type_1(value: str) -> DNSRecordDetailEffectiveCriticalityType1:
    if value in DNS_RECORD_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DNS_RECORD_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
