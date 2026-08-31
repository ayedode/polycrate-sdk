from typing import Literal

ApiV1AdminUsersPartialUpdateIsStaffErrorComponentAttr = Literal["is_staff"]

API_V1_ADMIN_USERS_PARTIAL_UPDATE_IS_STAFF_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AdminUsersPartialUpdateIsStaffErrorComponentAttr
] = {
    "is_staff",
}


def check_api_v1_admin_users_partial_update_is_staff_error_component_attr(
    value: str,
) -> ApiV1AdminUsersPartialUpdateIsStaffErrorComponentAttr:
    if value in API_V1_ADMIN_USERS_PARTIAL_UPDATE_IS_STAFF_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_PARTIAL_UPDATE_IS_STAFF_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
