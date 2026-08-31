from typing import Literal

ApiV1NotesPartialUpdateMeetingDurationMinutesErrorComponentAttr = Literal["meeting_duration_minutes"]

API_V1_NOTES_PARTIAL_UPDATE_MEETING_DURATION_MINUTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesPartialUpdateMeetingDurationMinutesErrorComponentAttr
] = {
    "meeting_duration_minutes",
}


def check_api_v1_notes_partial_update_meeting_duration_minutes_error_component_attr(
    value: str,
) -> ApiV1NotesPartialUpdateMeetingDurationMinutesErrorComponentAttr:
    if value in API_V1_NOTES_PARTIAL_UPDATE_MEETING_DURATION_MINUTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_PARTIAL_UPDATE_MEETING_DURATION_MINUTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
