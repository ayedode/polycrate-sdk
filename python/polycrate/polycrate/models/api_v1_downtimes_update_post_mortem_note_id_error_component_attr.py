from typing import Literal

ApiV1DowntimesUpdatePostMortemNoteIdErrorComponentAttr = Literal["post_mortem_note_id"]

API_V1_DOWNTIMES_UPDATE_POST_MORTEM_NOTE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DowntimesUpdatePostMortemNoteIdErrorComponentAttr
] = {
    "post_mortem_note_id",
}


def check_api_v1_downtimes_update_post_mortem_note_id_error_component_attr(
    value: str,
) -> ApiV1DowntimesUpdatePostMortemNoteIdErrorComponentAttr:
    if value in API_V1_DOWNTIMES_UPDATE_POST_MORTEM_NOTE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_UPDATE_POST_MORTEM_NOTE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
