from typing import Literal

ApiV1AdminUsersCreateEmailVerifiedErrorComponentCode = Literal["invalid", "null"]

API_V1_ADMIN_USERS_CREATE_EMAIL_VERIFIED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AdminUsersCreateEmailVerifiedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_admin_users_create_email_verified_error_component_code(
    value: str,
) -> ApiV1AdminUsersCreateEmailVerifiedErrorComponentCode:
    if value in API_V1_ADMIN_USERS_CREATE_EMAIL_VERIFIED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_CREATE_EMAIL_VERIFIED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
