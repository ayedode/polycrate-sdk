from typing import Literal

ApiV1NotesCreateMeetingDurationMinutesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_NOTES_CREATE_MEETING_DURATION_MINUTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesCreateMeetingDurationMinutesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_notes_create_meeting_duration_minutes_error_component_code(
    value: str,
) -> ApiV1NotesCreateMeetingDurationMinutesErrorComponentCode:
    if value in API_V1_NOTES_CREATE_MEETING_DURATION_MINUTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_CREATE_MEETING_DURATION_MINUTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
