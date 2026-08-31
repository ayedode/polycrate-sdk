from typing import Literal

ApiV1OrganizationsDiscoverCreatePriorityErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_PRIORITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsDiscoverCreatePriorityErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_discover_create_priority_error_component_code(
    value: str,
) -> ApiV1OrganizationsDiscoverCreatePriorityErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_PRIORITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_PRIORITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
