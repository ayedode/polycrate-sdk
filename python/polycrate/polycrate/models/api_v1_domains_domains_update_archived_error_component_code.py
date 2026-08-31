from typing import Literal

ApiV1DomainsDomainsUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DOMAINS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_domains_update_archived_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsUpdateArchivedErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
