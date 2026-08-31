from typing import Literal

ApiV1AdminUsersMembershipsCreateRoleErrorComponentAttr = Literal["role"]

API_V1_ADMIN_USERS_MEMBERSHIPS_CREATE_ROLE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AdminUsersMembershipsCreateRoleErrorComponentAttr
] = {
    "role",
}


def check_api_v1_admin_users_memberships_create_role_error_component_attr(
    value: str,
) -> ApiV1AdminUsersMembershipsCreateRoleErrorComponentAttr:
    if value in API_V1_ADMIN_USERS_MEMBERSHIPS_CREATE_ROLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_MEMBERSHIPS_CREATE_ROLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
