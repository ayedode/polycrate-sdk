from typing import Literal

ApiV1DomainsDomainsArchiveCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsArchiveCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_domains_domains_archive_create_criticality_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsArchiveCreateCriticalityErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
