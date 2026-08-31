from typing import Literal

ApiV1AdminUsersUpdateRoleErrorComponentCode = Literal["invalid_choice"]

API_V1_ADMIN_USERS_UPDATE_ROLE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AdminUsersUpdateRoleErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_admin_users_update_role_error_component_code(
    value: str,
) -> ApiV1AdminUsersUpdateRoleErrorComponentCode:
    if value in API_V1_ADMIN_USERS_UPDATE_ROLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_UPDATE_ROLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
