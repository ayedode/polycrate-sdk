from typing import Literal

ApiV1DomainsDnszonesDisableDnssecCreatePrimaryZoneErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_PRIMARY_ZONE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesDisableDnssecCreatePrimaryZoneErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_dnszones_disable_dnssec_create_primary_zone_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesDisableDnssecCreatePrimaryZoneErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_PRIMARY_ZONE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_PRIMARY_ZONE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
