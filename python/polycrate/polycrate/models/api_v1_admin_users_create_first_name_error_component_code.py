from typing import Literal

ApiV1AdminUsersCreateFirstNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ADMIN_USERS_CREATE_FIRST_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AdminUsersCreateFirstNameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_admin_users_create_first_name_error_component_code(
    value: str,
) -> ApiV1AdminUsersCreateFirstNameErrorComponentCode:
    if value in API_V1_ADMIN_USERS_CREATE_FIRST_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_CREATE_FIRST_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
