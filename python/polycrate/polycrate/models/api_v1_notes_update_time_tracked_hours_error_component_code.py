from typing import Literal

ApiV1NotesUpdateTimeTrackedHoursErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_NOTES_UPDATE_TIME_TRACKED_HOURS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesUpdateTimeTrackedHoursErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_notes_update_time_tracked_hours_error_component_code(
    value: str,
) -> ApiV1NotesUpdateTimeTrackedHoursErrorComponentCode:
    if value in API_V1_NOTES_UPDATE_TIME_TRACKED_HOURS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_UPDATE_TIME_TRACKED_HOURS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
