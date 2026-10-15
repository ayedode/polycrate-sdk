from typing import Literal

DNSRecordDetailEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

DNS_RECORD_DETAIL_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[DNSRecordDetailEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_dns_record_detail_effective_criticality_type_3_type_1(
    value: str,
) -> DNSRecordDetailEffectiveCriticalityType3Type1:
    if value in DNS_RECORD_DETAIL_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DNS_RECORD_DETAIL_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
