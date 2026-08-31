from typing import Literal

ApiV1ContactsPartialUpdateNoteErrorComponentAttr = Literal["note"]

API_V1_CONTACTS_PARTIAL_UPDATE_NOTE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsPartialUpdateNoteErrorComponentAttr
] = {
    "note",
}


def check_api_v1_contacts_partial_update_note_error_component_attr(
    value: str,
) -> ApiV1ContactsPartialUpdateNoteErrorComponentAttr:
    if value in API_V1_CONTACTS_PARTIAL_UPDATE_NOTE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_PARTIAL_UPDATE_NOTE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
