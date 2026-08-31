from typing import Literal

ApiV1DowntimesArchiveCreatePostMortemNoteIdErrorComponentCode = Literal["invalid"]

API_V1_DOWNTIMES_ARCHIVE_CREATE_POST_MORTEM_NOTE_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DowntimesArchiveCreatePostMortemNoteIdErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_downtimes_archive_create_post_mortem_note_id_error_component_code(
    value: str,
) -> ApiV1DowntimesArchiveCreatePostMortemNoteIdErrorComponentCode:
    if value in API_V1_DOWNTIMES_ARCHIVE_CREATE_POST_MORTEM_NOTE_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_ARCHIVE_CREATE_POST_MORTEM_NOTE_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
