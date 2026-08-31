from typing import Literal

ApiV1UsersPartialUpdateLastNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_USERS_PARTIAL_UPDATE_LAST_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1UsersPartialUpdateLastNameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_users_partial_update_last_name_error_component_code(
    value: str,
) -> ApiV1UsersPartialUpdateLastNameErrorComponentCode:
    if value in API_V1_USERS_PARTIAL_UPDATE_LAST_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_USERS_PARTIAL_UPDATE_LAST_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
