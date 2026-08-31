from typing import Literal

ApiV1AdminUsersPartialUpdateEmailErrorComponentAttr = Literal["email"]

API_V1_ADMIN_USERS_PARTIAL_UPDATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AdminUsersPartialUpdateEmailErrorComponentAttr
] = {
    "email",
}


def check_api_v1_admin_users_partial_update_email_error_component_attr(
    value: str,
) -> ApiV1AdminUsersPartialUpdateEmailErrorComponentAttr:
    if value in API_V1_ADMIN_USERS_PARTIAL_UPDATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_PARTIAL_UPDATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
