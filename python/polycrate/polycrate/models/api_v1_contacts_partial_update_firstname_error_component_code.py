from typing import Literal

ApiV1ContactsPartialUpdateFirstnameErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_CONTACTS_PARTIAL_UPDATE_FIRSTNAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ContactsPartialUpdateFirstnameErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_contacts_partial_update_firstname_error_component_code(
    value: str,
) -> ApiV1ContactsPartialUpdateFirstnameErrorComponentCode:
    if value in API_V1_CONTACTS_PARTIAL_UPDATE_FIRSTNAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_PARTIAL_UPDATE_FIRSTNAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
