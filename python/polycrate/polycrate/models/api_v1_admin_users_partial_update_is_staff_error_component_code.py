from typing import Literal

ApiV1AdminUsersPartialUpdateIsStaffErrorComponentCode = Literal["invalid", "null"]

API_V1_ADMIN_USERS_PARTIAL_UPDATE_IS_STAFF_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AdminUsersPartialUpdateIsStaffErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_admin_users_partial_update_is_staff_error_component_code(
    value: str,
) -> ApiV1AdminUsersPartialUpdateIsStaffErrorComponentCode:
    if value in API_V1_ADMIN_USERS_PARTIAL_UPDATE_IS_STAFF_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_PARTIAL_UPDATE_IS_STAFF_ERROR_COMPONENT_CODE_VALUES!r}"
    )
