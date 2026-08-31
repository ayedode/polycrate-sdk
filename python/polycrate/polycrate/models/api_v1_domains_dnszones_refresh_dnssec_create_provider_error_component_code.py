from typing import Literal

ApiV1DomainsDnszonesRefreshDnssecCreateProviderErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesRefreshDnssecCreateProviderErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_domains_dnszones_refresh_dnssec_create_provider_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesRefreshDnssecCreateProviderErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
