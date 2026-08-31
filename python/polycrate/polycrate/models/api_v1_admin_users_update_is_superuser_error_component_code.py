from typing import Literal

ApiV1AdminUsersUpdateIsSuperuserErrorComponentCode = Literal["invalid", "null"]

API_V1_ADMIN_USERS_UPDATE_IS_SUPERUSER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AdminUsersUpdateIsSuperuserErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_admin_users_update_is_superuser_error_component_code(
    value: str,
) -> ApiV1AdminUsersUpdateIsSuperuserErrorComponentCode:
    if value in API_V1_ADMIN_USERS_UPDATE_IS_SUPERUSER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_UPDATE_IS_SUPERUSER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
