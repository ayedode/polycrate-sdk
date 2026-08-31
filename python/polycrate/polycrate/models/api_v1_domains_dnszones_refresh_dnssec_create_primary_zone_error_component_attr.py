from typing import Literal

ApiV1DomainsDnszonesRefreshDnssecCreatePrimaryZoneErrorComponentAttr = Literal["primary_zone"]

API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_PRIMARY_ZONE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRefreshDnssecCreatePrimaryZoneErrorComponentAttr
] = {
    "primary_zone",
}


def check_api_v1_domains_dnszones_refresh_dnssec_create_primary_zone_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRefreshDnssecCreatePrimaryZoneErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_PRIMARY_ZONE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_PRIMARY_ZONE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
