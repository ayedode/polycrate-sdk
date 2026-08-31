from typing import Literal

ApiV1DomainsDomainRegistrarsPartialUpdateLastRateLimitedAtErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsPartialUpdateLastRateLimitedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_domains_domain_registrars_partial_update_last_rate_limited_at_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsPartialUpdateLastRateLimitedAtErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
