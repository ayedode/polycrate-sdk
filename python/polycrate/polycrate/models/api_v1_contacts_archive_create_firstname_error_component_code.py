from typing import Literal

ApiV1ContactsArchiveCreateFirstnameErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_CONTACTS_ARCHIVE_CREATE_FIRSTNAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ContactsArchiveCreateFirstnameErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_contacts_archive_create_firstname_error_component_code(
    value: str,
) -> ApiV1ContactsArchiveCreateFirstnameErrorComponentCode:
    if value in API_V1_CONTACTS_ARCHIVE_CREATE_FIRSTNAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_ARCHIVE_CREATE_FIRSTNAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
