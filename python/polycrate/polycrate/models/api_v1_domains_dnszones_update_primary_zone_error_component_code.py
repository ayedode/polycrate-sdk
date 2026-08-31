from typing import Literal

ApiV1DomainsDnszonesUpdatePrimaryZoneErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DNSZONES_UPDATE_PRIMARY_ZONE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesUpdatePrimaryZoneErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_dnszones_update_primary_zone_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesUpdatePrimaryZoneErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_UPDATE_PRIMARY_ZONE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_UPDATE_PRIMARY_ZONE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
