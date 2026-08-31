from typing import Literal

ApiV1OrganizationsDiscoverCreateCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsDiscoverCreateCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_organizations_discover_create_created_by_component_error_component_code(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateCreatedByComponentErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
