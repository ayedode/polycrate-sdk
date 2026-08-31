from typing import Literal

ApiV1NotesPartialUpdateTrackedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_NOTES_PARTIAL_UPDATE_TRACKED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesPartialUpdateTrackedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_notes_partial_update_tracked_at_error_component_code(
    value: str,
) -> ApiV1NotesPartialUpdateTrackedAtErrorComponentCode:
    if value in API_V1_NOTES_PARTIAL_UPDATE_TRACKED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_PARTIAL_UPDATE_TRACKED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
