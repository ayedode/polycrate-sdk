from typing import Literal

ApiV1UsersMembershipsCreateRoleErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_USERS_MEMBERSHIPS_CREATE_ROLE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1UsersMembershipsCreateRoleErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_users_memberships_create_role_error_component_code(
    value: str,
) -> ApiV1UsersMembershipsCreateRoleErrorComponentCode:
    if value in API_V1_USERS_MEMBERSHIPS_CREATE_ROLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_USERS_MEMBERSHIPS_CREATE_ROLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
