from typing import Literal

ApiV1ContactsCreateNameErrorComponentCode = Literal[
    "blank", "invalid", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_CONTACTS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ContactsCreateNameErrorComponentCode] = {
    "blank",
    "invalid",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_contacts_create_name_error_component_code(value: str) -> ApiV1ContactsCreateNameErrorComponentCode:
    if value in API_V1_CONTACTS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
