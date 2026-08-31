from typing import Literal

ApiV1ContactsUpdateNoteErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CONTACTS_UPDATE_NOTE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ContactsUpdateNoteErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_contacts_update_note_error_component_code(value: str) -> ApiV1ContactsUpdateNoteErrorComponentCode:
    if value in API_V1_CONTACTS_UPDATE_NOTE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_UPDATE_NOTE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
