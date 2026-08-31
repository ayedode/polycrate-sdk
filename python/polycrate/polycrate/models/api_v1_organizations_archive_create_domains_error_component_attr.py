from typing import Literal

ApiV1OrganizationsArchiveCreateDomainsErrorComponentAttr = Literal["domains"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_DOMAINS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateDomainsErrorComponentAttr
] = {
    "domains",
}


def check_api_v1_organizations_archive_create_domains_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateDomainsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_DOMAINS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_DOMAINS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
