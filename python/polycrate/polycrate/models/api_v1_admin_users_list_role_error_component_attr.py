from typing import Literal

ApiV1AdminUsersListRoleErrorComponentAttr = Literal["role"]

API_V1_ADMIN_USERS_LIST_ROLE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AdminUsersListRoleErrorComponentAttr] = {
    "role",
}


def check_api_v1_admin_users_list_role_error_component_attr(value: str) -> ApiV1AdminUsersListRoleErrorComponentAttr:
    if value in API_V1_ADMIN_USERS_LIST_ROLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_LIST_ROLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
