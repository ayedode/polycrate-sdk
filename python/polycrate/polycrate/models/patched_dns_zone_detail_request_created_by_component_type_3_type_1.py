from typing import Literal

PatchedDNSZoneDetailRequestCreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

PATCHED_DNS_ZONE_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[
    PatchedDNSZoneDetailRequestCreatedByComponentType3Type1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_patched_dns_zone_detail_request_created_by_component_type_3_type_1(
    value: str,
) -> PatchedDNSZoneDetailRequestCreatedByComponentType3Type1:
    if value in PATCHED_DNS_ZONE_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_DNS_ZONE_DETAIL_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}"
    )
