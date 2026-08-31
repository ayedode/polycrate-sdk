from typing import Literal

ApiV1DowntimesCreatePostMortemNoteIdErrorComponentAttr = Literal["post_mortem_note_id"]

API_V1_DOWNTIMES_CREATE_POST_MORTEM_NOTE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DowntimesCreatePostMortemNoteIdErrorComponentAttr
] = {
    "post_mortem_note_id",
}


def check_api_v1_downtimes_create_post_mortem_note_id_error_component_attr(
    value: str,
) -> ApiV1DowntimesCreatePostMortemNoteIdErrorComponentAttr:
    if value in API_V1_DOWNTIMES_CREATE_POST_MORTEM_NOTE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_CREATE_POST_MORTEM_NOTE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
