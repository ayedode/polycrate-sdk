from typing import Literal

ApiV1NotesUpdateMeetingDurationMinutesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_NOTES_UPDATE_MEETING_DURATION_MINUTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesUpdateMeetingDurationMinutesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_notes_update_meeting_duration_minutes_error_component_code(
    value: str,
) -> ApiV1NotesUpdateMeetingDurationMinutesErrorComponentCode:
    if value in API_V1_NOTES_UPDATE_MEETING_DURATION_MINUTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_UPDATE_MEETING_DURATION_MINUTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
