from typing import Literal

ApiV1OrganizationsDiscoverCreateCreatedByUserErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_CREATED_BY_USER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsDiscoverCreateCreatedByUserErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_organizations_discover_create_created_by_user_error_component_code(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateCreatedByUserErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_CREATED_BY_USER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_CREATED_BY_USER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
