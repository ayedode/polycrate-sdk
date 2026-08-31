from typing import Literal

ApiV1AdminUsersPartialUpdateRoleErrorComponentAttr = Literal["role"]

API_V1_ADMIN_USERS_PARTIAL_UPDATE_ROLE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AdminUsersPartialUpdateRoleErrorComponentAttr
] = {
    "role",
}


def check_api_v1_admin_users_partial_update_role_error_component_attr(
    value: str,
) -> ApiV1AdminUsersPartialUpdateRoleErrorComponentAttr:
    if value in API_V1_ADMIN_USERS_PARTIAL_UPDATE_ROLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_PARTIAL_UPDATE_ROLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
