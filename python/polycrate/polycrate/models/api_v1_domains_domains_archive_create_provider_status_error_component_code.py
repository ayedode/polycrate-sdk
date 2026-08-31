from typing import Literal

ApiV1DomainsDomainsArchiveCreateProviderStatusErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_PROVIDER_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsArchiveCreateProviderStatusErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_domains_domains_archive_create_provider_status_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsArchiveCreateProviderStatusErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_PROVIDER_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_PROVIDER_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
