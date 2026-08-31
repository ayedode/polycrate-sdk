from typing import Literal

ApiV1UsersMembershipsPartialUpdateRoleErrorComponentCode = Literal["invalid_choice", "null", "required"]

API_V1_USERS_MEMBERSHIPS_PARTIAL_UPDATE_ROLE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1UsersMembershipsPartialUpdateRoleErrorComponentCode
] = {
    "invalid_choice",
    "null",
    "required",
}


def check_api_v1_users_memberships_partial_update_role_error_component_code(
    value: str,
) -> ApiV1UsersMembershipsPartialUpdateRoleErrorComponentCode:
    if value in API_V1_USERS_MEMBERSHIPS_PARTIAL_UPDATE_ROLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_USERS_MEMBERSHIPS_PARTIAL_UPDATE_ROLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
