from typing import Literal

ApiV1DomainsDnszonesRefreshDnssecCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesRefreshDnssecCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_domains_dnszones_refresh_dnssec_create_kind_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesRefreshDnssecCreateKindErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
