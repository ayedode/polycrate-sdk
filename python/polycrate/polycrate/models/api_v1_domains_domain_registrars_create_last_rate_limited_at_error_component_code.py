from typing import Literal

ApiV1DomainsDomainRegistrarsCreateLastRateLimitedAtErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateLastRateLimitedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_domains_domain_registrars_create_last_rate_limited_at_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateLastRateLimitedAtErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
