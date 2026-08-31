from typing import Literal

ApiV1OrganizationsDiscoverCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_organizations_discover_create_scope_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateScopeErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
