from typing import Literal

DNSZoneDetailRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

DNS_ZONE_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[DNSZoneDetailRequestCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_dns_zone_detail_request_criticality_type_3_type_1(value: str) -> DNSZoneDetailRequestCriticalityType3Type1:
    if value in DNS_ZONE_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DNS_ZONE_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
