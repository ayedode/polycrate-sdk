from typing import Literal

ApiV1AdminUsersUpdateIsStaffErrorComponentCode = Literal["invalid", "null"]

API_V1_ADMIN_USERS_UPDATE_IS_STAFF_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AdminUsersUpdateIsStaffErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_admin_users_update_is_staff_error_component_code(
    value: str,
) -> ApiV1AdminUsersUpdateIsStaffErrorComponentCode:
    if value in API_V1_ADMIN_USERS_UPDATE_IS_STAFF_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_UPDATE_IS_STAFF_ERROR_COMPONENT_CODE_VALUES!r}"
    )
