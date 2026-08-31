from typing import Literal

ApiV1OrganizationsArchiveCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_organizations_archive_create_scope_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateScopeErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
