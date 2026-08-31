from typing import Literal

ApiV1OrganizationsDiscoverCreateModifiedByUserErrorComponentAttr = Literal["modified_by_user"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateModifiedByUserErrorComponentAttr
] = {
    "modified_by_user",
}


def check_api_v1_organizations_discover_create_modified_by_user_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateModifiedByUserErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
