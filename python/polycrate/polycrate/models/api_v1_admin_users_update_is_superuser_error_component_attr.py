from typing import Literal

ApiV1AdminUsersUpdateIsSuperuserErrorComponentAttr = Literal["is_superuser"]

API_V1_ADMIN_USERS_UPDATE_IS_SUPERUSER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AdminUsersUpdateIsSuperuserErrorComponentAttr
] = {
    "is_superuser",
}


def check_api_v1_admin_users_update_is_superuser_error_component_attr(
    value: str,
) -> ApiV1AdminUsersUpdateIsSuperuserErrorComponentAttr:
    if value in API_V1_ADMIN_USERS_UPDATE_IS_SUPERUSER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_UPDATE_IS_SUPERUSER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
