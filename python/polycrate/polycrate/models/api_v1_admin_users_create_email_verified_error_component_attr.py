from typing import Literal

ApiV1AdminUsersCreateEmailVerifiedErrorComponentAttr = Literal["email_verified"]

API_V1_ADMIN_USERS_CREATE_EMAIL_VERIFIED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AdminUsersCreateEmailVerifiedErrorComponentAttr
] = {
    "email_verified",
}


def check_api_v1_admin_users_create_email_verified_error_component_attr(
    value: str,
) -> ApiV1AdminUsersCreateEmailVerifiedErrorComponentAttr:
    if value in API_V1_ADMIN_USERS_CREATE_EMAIL_VERIFIED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_CREATE_EMAIL_VERIFIED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
