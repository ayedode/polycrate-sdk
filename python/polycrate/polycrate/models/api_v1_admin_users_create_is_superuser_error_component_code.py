from typing import Literal

ApiV1AdminUsersCreateIsSuperuserErrorComponentCode = Literal["invalid", "null"]

API_V1_ADMIN_USERS_CREATE_IS_SUPERUSER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AdminUsersCreateIsSuperuserErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_admin_users_create_is_superuser_error_component_code(
    value: str,
) -> ApiV1AdminUsersCreateIsSuperuserErrorComponentCode:
    if value in API_V1_ADMIN_USERS_CREATE_IS_SUPERUSER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_CREATE_IS_SUPERUSER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
