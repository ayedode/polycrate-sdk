from typing import Literal

PatchedDNSZoneDetailRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PATCHED_DNS_ZONE_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    PatchedDNSZoneDetailRequestCriticalityType2Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_dns_zone_detail_request_criticality_type_2_type_1(
    value: str,
) -> PatchedDNSZoneDetailRequestCriticalityType2Type1:
    if value in PATCHED_DNS_ZONE_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_DNS_ZONE_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
