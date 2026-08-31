from typing import Literal

ApiV1DomainsDnszonesUpdatePrimaryZoneErrorComponentAttr = Literal["primary_zone"]

API_V1_DOMAINS_DNSZONES_UPDATE_PRIMARY_ZONE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesUpdatePrimaryZoneErrorComponentAttr
] = {
    "primary_zone",
}


def check_api_v1_domains_dnszones_update_primary_zone_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesUpdatePrimaryZoneErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_UPDATE_PRIMARY_ZONE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_UPDATE_PRIMARY_ZONE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
