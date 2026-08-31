from typing import Literal

ApiV1AdminUsersListOrganizationErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_ADMIN_USERS_LIST_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AdminUsersListOrganizationErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_admin_users_list_organization_error_component_code(
    value: str,
) -> ApiV1AdminUsersListOrganizationErrorComponentCode:
    if value in API_V1_ADMIN_USERS_LIST_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_LIST_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
