from typing import Literal

ApiV1OrganizationsArchiveCreateDomainsErrorComponentCode = Literal["invalid"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_DOMAINS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsArchiveCreateDomainsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_organizations_archive_create_domains_error_component_code(
    value: str,
) -> ApiV1OrganizationsArchiveCreateDomainsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_DOMAINS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_DOMAINS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
