from typing import Literal

ApiV1ContactsUpdateZipcodeErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CONTACTS_UPDATE_ZIPCODE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ContactsUpdateZipcodeErrorComponentCode] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_contacts_update_zipcode_error_component_code(
    value: str,
) -> ApiV1ContactsUpdateZipcodeErrorComponentCode:
    if value in API_V1_CONTACTS_UPDATE_ZIPCODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_UPDATE_ZIPCODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
