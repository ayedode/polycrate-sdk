from typing import Literal

ApiV1UsersMembershipsPartialUpdateRoleErrorComponentAttr = Literal["role"]

API_V1_USERS_MEMBERSHIPS_PARTIAL_UPDATE_ROLE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1UsersMembershipsPartialUpdateRoleErrorComponentAttr
] = {
    "role",
}


def check_api_v1_users_memberships_partial_update_role_error_component_attr(
    value: str,
) -> ApiV1UsersMembershipsPartialUpdateRoleErrorComponentAttr:
    if value in API_V1_USERS_MEMBERSHIPS_PARTIAL_UPDATE_ROLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_USERS_MEMBERSHIPS_PARTIAL_UPDATE_ROLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
