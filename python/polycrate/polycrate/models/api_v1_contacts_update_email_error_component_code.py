from typing import Literal

ApiV1ContactsUpdateEmailErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_CONTACTS_UPDATE_EMAIL_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ContactsUpdateEmailErrorComponentCode] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_contacts_update_email_error_component_code(value: str) -> ApiV1ContactsUpdateEmailErrorComponentCode:
    if value in API_V1_CONTACTS_UPDATE_EMAIL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_UPDATE_EMAIL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
