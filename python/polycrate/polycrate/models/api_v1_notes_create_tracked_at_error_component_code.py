from typing import Literal

ApiV1NotesCreateTrackedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_NOTES_CREATE_TRACKED_AT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1NotesCreateTrackedAtErrorComponentCode] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_notes_create_tracked_at_error_component_code(
    value: str,
) -> ApiV1NotesCreateTrackedAtErrorComponentCode:
    if value in API_V1_NOTES_CREATE_TRACKED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_CREATE_TRACKED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
