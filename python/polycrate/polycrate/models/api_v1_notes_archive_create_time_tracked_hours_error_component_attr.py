from typing import Literal

ApiV1NotesArchiveCreateTimeTrackedHoursErrorComponentAttr = Literal["time_tracked_hours"]

API_V1_NOTES_ARCHIVE_CREATE_TIME_TRACKED_HOURS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesArchiveCreateTimeTrackedHoursErrorComponentAttr
] = {
    "time_tracked_hours",
}


def check_api_v1_notes_archive_create_time_tracked_hours_error_component_attr(
    value: str,
) -> ApiV1NotesArchiveCreateTimeTrackedHoursErrorComponentAttr:
    if value in API_V1_NOTES_ARCHIVE_CREATE_TIME_TRACKED_HOURS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_ARCHIVE_CREATE_TIME_TRACKED_HOURS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
