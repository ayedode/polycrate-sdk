from typing import Literal

ApiV1DowntimesUpdatePostMortemNoteIdErrorComponentCode = Literal["invalid"]

API_V1_DOWNTIMES_UPDATE_POST_MORTEM_NOTE_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DowntimesUpdatePostMortemNoteIdErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_downtimes_update_post_mortem_note_id_error_component_code(
    value: str,
) -> ApiV1DowntimesUpdatePostMortemNoteIdErrorComponentCode:
    if value in API_V1_DOWNTIMES_UPDATE_POST_MORTEM_NOTE_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_UPDATE_POST_MORTEM_NOTE_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
