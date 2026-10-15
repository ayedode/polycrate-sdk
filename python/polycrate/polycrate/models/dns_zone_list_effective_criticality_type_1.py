from typing import Literal

DNSZoneListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

DNS_ZONE_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[DNSZoneListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_dns_zone_list_effective_criticality_type_1(value: str) -> DNSZoneListEffectiveCriticalityType1:
    if value in DNS_ZONE_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DNS_ZONE_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
