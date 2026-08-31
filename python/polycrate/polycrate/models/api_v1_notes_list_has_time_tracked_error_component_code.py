from typing import Literal

ApiV1NotesListHasTimeTrackedErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_NOTES_LIST_HAS_TIME_TRACKED_ERROR_COMPONENT_CODE_VALUES: set[ApiV1NotesListHasTimeTrackedErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_notes_list_has_time_tracked_error_component_code(
    value: str,
) -> ApiV1NotesListHasTimeTrackedErrorComponentCode:
    if value in API_V1_NOTES_LIST_HAS_TIME_TRACKED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_LIST_HAS_TIME_TRACKED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
