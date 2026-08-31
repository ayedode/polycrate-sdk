from typing import Literal

ApiV1NotesRescanProviderStatusCreateMeetingDurationMinutesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_MEETING_DURATION_MINUTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateMeetingDurationMinutesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_notes_rescan_provider_status_create_meeting_duration_minutes_error_component_code(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateMeetingDurationMinutesErrorComponentCode:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_MEETING_DURATION_MINUTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_MEETING_DURATION_MINUTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
