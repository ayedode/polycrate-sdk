from typing import Literal

ApiV1AdminUsersCreateEmailErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
    "unique",
]

API_V1_ADMIN_USERS_CREATE_EMAIL_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AdminUsersCreateEmailErrorComponentCode] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
    "unique",
}


def check_api_v1_admin_users_create_email_error_component_code(
    value: str,
) -> ApiV1AdminUsersCreateEmailErrorComponentCode:
    if value in API_V1_ADMIN_USERS_CREATE_EMAIL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_CREATE_EMAIL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
