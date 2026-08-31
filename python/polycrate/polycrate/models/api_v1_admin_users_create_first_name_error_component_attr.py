from typing import Literal

ApiV1AdminUsersCreateFirstNameErrorComponentAttr = Literal["first_name"]

API_V1_ADMIN_USERS_CREATE_FIRST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AdminUsersCreateFirstNameErrorComponentAttr
] = {
    "first_name",
}


def check_api_v1_admin_users_create_first_name_error_component_attr(
    value: str,
) -> ApiV1AdminUsersCreateFirstNameErrorComponentAttr:
    if value in API_V1_ADMIN_USERS_CREATE_FIRST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_CREATE_FIRST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
