from typing import Literal

ApiV1AdminUsersPartialUpdateRoleErrorComponentCode = Literal["invalid_choice"]

API_V1_ADMIN_USERS_PARTIAL_UPDATE_ROLE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AdminUsersPartialUpdateRoleErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_admin_users_partial_update_role_error_component_code(
    value: str,
) -> ApiV1AdminUsersPartialUpdateRoleErrorComponentCode:
    if value in API_V1_ADMIN_USERS_PARTIAL_UPDATE_ROLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_PARTIAL_UPDATE_ROLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
