from typing import Literal

ApiV1DowntimesPartialUpdatePostMortemNoteIdErrorComponentCode = Literal["invalid"]

API_V1_DOWNTIMES_PARTIAL_UPDATE_POST_MORTEM_NOTE_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DowntimesPartialUpdatePostMortemNoteIdErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_downtimes_partial_update_post_mortem_note_id_error_component_code(
    value: str,
) -> ApiV1DowntimesPartialUpdatePostMortemNoteIdErrorComponentCode:
    if value in API_V1_DOWNTIMES_PARTIAL_UPDATE_POST_MORTEM_NOTE_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_PARTIAL_UPDATE_POST_MORTEM_NOTE_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
