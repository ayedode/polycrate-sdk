from typing import Literal

ApiV1AdminUsersCreateEmailErrorComponentAttr = Literal["email"]

API_V1_ADMIN_USERS_CREATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AdminUsersCreateEmailErrorComponentAttr] = {
    "email",
}


def check_api_v1_admin_users_create_email_error_component_attr(
    value: str,
) -> ApiV1AdminUsersCreateEmailErrorComponentAttr:
    if value in API_V1_ADMIN_USERS_CREATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_CREATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
