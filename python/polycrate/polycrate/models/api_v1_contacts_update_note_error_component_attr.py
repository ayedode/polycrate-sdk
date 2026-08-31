from typing import Literal

ApiV1ContactsUpdateNoteErrorComponentAttr = Literal["note"]

API_V1_CONTACTS_UPDATE_NOTE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ContactsUpdateNoteErrorComponentAttr] = {
    "note",
}


def check_api_v1_contacts_update_note_error_component_attr(value: str) -> ApiV1ContactsUpdateNoteErrorComponentAttr:
    if value in API_V1_CONTACTS_UPDATE_NOTE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_UPDATE_NOTE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
