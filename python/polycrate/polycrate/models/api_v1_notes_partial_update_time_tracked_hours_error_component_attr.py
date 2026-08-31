from typing import Literal

ApiV1NotesPartialUpdateTimeTrackedHoursErrorComponentAttr = Literal["time_tracked_hours"]

API_V1_NOTES_PARTIAL_UPDATE_TIME_TRACKED_HOURS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesPartialUpdateTimeTrackedHoursErrorComponentAttr
] = {
    "time_tracked_hours",
}


def check_api_v1_notes_partial_update_time_tracked_hours_error_component_attr(
    value: str,
) -> ApiV1NotesPartialUpdateTimeTrackedHoursErrorComponentAttr:
    if value in API_V1_NOTES_PARTIAL_UPDATE_TIME_TRACKED_HOURS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_PARTIAL_UPDATE_TIME_TRACKED_HOURS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
