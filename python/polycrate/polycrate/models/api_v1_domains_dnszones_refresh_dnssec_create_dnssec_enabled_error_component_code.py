from typing import Literal

ApiV1DomainsDnszonesRefreshDnssecCreateDnssecEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_DNSSEC_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesRefreshDnssecCreateDnssecEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_dnszones_refresh_dnssec_create_dnssec_enabled_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesRefreshDnssecCreateDnssecEnabledErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_DNSSEC_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_DNSSEC_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
