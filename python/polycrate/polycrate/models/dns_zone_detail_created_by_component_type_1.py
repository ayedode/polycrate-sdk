from typing import Literal

DNSZoneDetailCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

DNS_ZONE_DETAIL_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[DNSZoneDetailCreatedByComponentType1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_dns_zone_detail_created_by_component_type_1(value: str) -> DNSZoneDetailCreatedByComponentType1:
    if value in DNS_ZONE_DETAIL_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DNS_ZONE_DETAIL_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}"
    )
