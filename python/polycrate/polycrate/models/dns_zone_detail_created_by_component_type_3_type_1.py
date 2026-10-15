from typing import Literal

DNSZoneDetailCreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

DNS_ZONE_DETAIL_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[DNSZoneDetailCreatedByComponentType3Type1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_dns_zone_detail_created_by_component_type_3_type_1(value: str) -> DNSZoneDetailCreatedByComponentType3Type1:
    if value in DNS_ZONE_DETAIL_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DNS_ZONE_DETAIL_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}"
    )
