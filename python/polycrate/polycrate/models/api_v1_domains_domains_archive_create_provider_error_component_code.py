from typing import Literal

ApiV1DomainsDomainsArchiveCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsArchiveCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_domains_domains_archive_create_provider_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsArchiveCreateProviderErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
