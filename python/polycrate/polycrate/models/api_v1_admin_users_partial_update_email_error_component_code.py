from typing import Literal

ApiV1AdminUsersPartialUpdateEmailErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
    "unique",
]

API_V1_ADMIN_USERS_PARTIAL_UPDATE_EMAIL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AdminUsersPartialUpdateEmailErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
    "unique",
}


def check_api_v1_admin_users_partial_update_email_error_component_code(
    value: str,
) -> ApiV1AdminUsersPartialUpdateEmailErrorComponentCode:
    if value in API_V1_ADMIN_USERS_PARTIAL_UPDATE_EMAIL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_PARTIAL_UPDATE_EMAIL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
