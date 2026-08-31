from typing import Literal

ApiV1NotesRescanProviderStatusCreateTimeTrackedHoursErrorComponentAttr = Literal["time_tracked_hours"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_TIME_TRACKED_HOURS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateTimeTrackedHoursErrorComponentAttr
] = {
    "time_tracked_hours",
}


def check_api_v1_notes_rescan_provider_status_create_time_tracked_hours_error_component_attr(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateTimeTrackedHoursErrorComponentAttr:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_TIME_TRACKED_HOURS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_TIME_TRACKED_HOURS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
