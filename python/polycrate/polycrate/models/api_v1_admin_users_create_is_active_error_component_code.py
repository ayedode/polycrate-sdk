from typing import Literal

ApiV1AdminUsersCreateIsActiveErrorComponentCode = Literal["invalid", "null"]

API_V1_ADMIN_USERS_CREATE_IS_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AdminUsersCreateIsActiveErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_admin_users_create_is_active_error_component_code(
    value: str,
) -> ApiV1AdminUsersCreateIsActiveErrorComponentCode:
    if value in API_V1_ADMIN_USERS_CREATE_IS_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_CREATE_IS_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
