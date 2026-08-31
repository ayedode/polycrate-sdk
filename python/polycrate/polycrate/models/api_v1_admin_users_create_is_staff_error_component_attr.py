from typing import Literal

ApiV1AdminUsersCreateIsStaffErrorComponentAttr = Literal["is_staff"]

API_V1_ADMIN_USERS_CREATE_IS_STAFF_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AdminUsersCreateIsStaffErrorComponentAttr] = {
    "is_staff",
}


def check_api_v1_admin_users_create_is_staff_error_component_attr(
    value: str,
) -> ApiV1AdminUsersCreateIsStaffErrorComponentAttr:
    if value in API_V1_ADMIN_USERS_CREATE_IS_STAFF_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_CREATE_IS_STAFF_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
