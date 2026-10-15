from typing import Literal

DNSRecordListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

DNS_RECORD_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[DNSRecordListEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_dns_record_list_effective_criticality_type_2_type_1(
    value: str,
) -> DNSRecordListEffectiveCriticalityType2Type1:
    if value in DNS_RECORD_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DNS_RECORD_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
