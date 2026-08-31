from typing import Literal

ApiV1AdminUsersUpdateRoleErrorComponentAttr = Literal["role"]

API_V1_ADMIN_USERS_UPDATE_ROLE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AdminUsersUpdateRoleErrorComponentAttr] = {
    "role",
}


def check_api_v1_admin_users_update_role_error_component_attr(
    value: str,
) -> ApiV1AdminUsersUpdateRoleErrorComponentAttr:
    if value in API_V1_ADMIN_USERS_UPDATE_ROLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_UPDATE_ROLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
