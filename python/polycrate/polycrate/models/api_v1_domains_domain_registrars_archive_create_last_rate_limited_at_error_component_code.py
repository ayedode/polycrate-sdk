from typing import Literal

ApiV1DomainsDomainRegistrarsArchiveCreateLastRateLimitedAtErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsArchiveCreateLastRateLimitedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_domains_domain_registrars_archive_create_last_rate_limited_at_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsArchiveCreateLastRateLimitedAtErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
