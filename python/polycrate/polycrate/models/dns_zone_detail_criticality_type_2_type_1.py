from typing import Literal

DNSZoneDetailCriticalityType2Type1 = Literal["", "high", "low", "medium"]

DNS_ZONE_DETAIL_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[DNSZoneDetailCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_dns_zone_detail_criticality_type_2_type_1(value: str) -> DNSZoneDetailCriticalityType2Type1:
    if value in DNS_ZONE_DETAIL_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNS_ZONE_DETAIL_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
