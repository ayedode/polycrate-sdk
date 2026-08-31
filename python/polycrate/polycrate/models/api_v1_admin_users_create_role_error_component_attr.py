from typing import Literal

ApiV1AdminUsersCreateRoleErrorComponentAttr = Literal["role"]

API_V1_ADMIN_USERS_CREATE_ROLE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AdminUsersCreateRoleErrorComponentAttr] = {
    "role",
}


def check_api_v1_admin_users_create_role_error_component_attr(
    value: str,
) -> ApiV1AdminUsersCreateRoleErrorComponentAttr:
    if value in API_V1_ADMIN_USERS_CREATE_ROLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_CREATE_ROLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
