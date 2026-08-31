from typing import Literal

ApiV1AdminUsersCreateIsSuperuserErrorComponentAttr = Literal["is_superuser"]

API_V1_ADMIN_USERS_CREATE_IS_SUPERUSER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AdminUsersCreateIsSuperuserErrorComponentAttr
] = {
    "is_superuser",
}


def check_api_v1_admin_users_create_is_superuser_error_component_attr(
    value: str,
) -> ApiV1AdminUsersCreateIsSuperuserErrorComponentAttr:
    if value in API_V1_ADMIN_USERS_CREATE_IS_SUPERUSER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_CREATE_IS_SUPERUSER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
