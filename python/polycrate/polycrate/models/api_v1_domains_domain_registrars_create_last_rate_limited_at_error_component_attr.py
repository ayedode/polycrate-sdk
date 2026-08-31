from typing import Literal

ApiV1DomainsDomainRegistrarsCreateLastRateLimitedAtErrorComponentAttr = Literal["last_rate_limited_at"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateLastRateLimitedAtErrorComponentAttr
] = {
    "last_rate_limited_at",
}


def check_api_v1_domains_domain_registrars_create_last_rate_limited_at_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateLastRateLimitedAtErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
