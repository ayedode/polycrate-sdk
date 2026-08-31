from typing import Literal

ApiV1OrganizationsDiscoverCreatePriorityErrorComponentAttr = Literal["priority"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreatePriorityErrorComponentAttr
] = {
    "priority",
}


def check_api_v1_organizations_discover_create_priority_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreatePriorityErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
