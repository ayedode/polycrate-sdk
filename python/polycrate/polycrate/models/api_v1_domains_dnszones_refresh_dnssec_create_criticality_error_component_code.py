from typing import Literal

ApiV1DomainsDnszonesRefreshDnssecCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesRefreshDnssecCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_domains_dnszones_refresh_dnssec_create_criticality_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesRefreshDnssecCreateCriticalityErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
