from typing import Literal

ApiV1NotesArchiveCreateMeetingDurationMinutesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_NOTES_ARCHIVE_CREATE_MEETING_DURATION_MINUTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesArchiveCreateMeetingDurationMinutesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_notes_archive_create_meeting_duration_minutes_error_component_code(
    value: str,
) -> ApiV1NotesArchiveCreateMeetingDurationMinutesErrorComponentCode:
    if value in API_V1_NOTES_ARCHIVE_CREATE_MEETING_DURATION_MINUTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_ARCHIVE_CREATE_MEETING_DURATION_MINUTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
