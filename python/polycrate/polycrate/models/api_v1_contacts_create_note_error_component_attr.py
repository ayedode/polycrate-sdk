from typing import Literal

ApiV1ContactsCreateNoteErrorComponentAttr = Literal["note"]

API_V1_CONTACTS_CREATE_NOTE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ContactsCreateNoteErrorComponentAttr] = {
    "note",
}


def check_api_v1_contacts_create_note_error_component_attr(value: str) -> ApiV1ContactsCreateNoteErrorComponentAttr:
    if value in API_V1_CONTACTS_CREATE_NOTE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_CREATE_NOTE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
