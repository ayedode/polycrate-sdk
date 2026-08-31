from typing import Literal

ApiV1AdminUsersCreateRoleErrorComponentCode = Literal["invalid_choice"]

API_V1_ADMIN_USERS_CREATE_ROLE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AdminUsersCreateRoleErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_admin_users_create_role_error_component_code(
    value: str,
) -> ApiV1AdminUsersCreateRoleErrorComponentCode:
    if value in API_V1_ADMIN_USERS_CREATE_ROLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_CREATE_ROLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
