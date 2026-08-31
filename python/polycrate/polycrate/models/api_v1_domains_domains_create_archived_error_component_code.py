from typing import Literal

ApiV1DomainsDomainsCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DOMAINS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_domains_create_archived_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsCreateArchivedErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
