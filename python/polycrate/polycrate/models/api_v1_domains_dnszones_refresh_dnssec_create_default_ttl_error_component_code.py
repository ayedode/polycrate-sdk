from typing import Literal

ApiV1DomainsDnszonesRefreshDnssecCreateDefaultTtlErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_DEFAULT_TTL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesRefreshDnssecCreateDefaultTtlErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_domains_dnszones_refresh_dnssec_create_default_ttl_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesRefreshDnssecCreateDefaultTtlErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_DEFAULT_TTL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_DEFAULT_TTL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
