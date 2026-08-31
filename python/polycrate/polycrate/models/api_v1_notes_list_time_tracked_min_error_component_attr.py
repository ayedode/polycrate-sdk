from typing import Literal

ApiV1NotesListTimeTrackedMinErrorComponentAttr = Literal["time_tracked_min"]

API_V1_NOTES_LIST_TIME_TRACKED_MIN_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesListTimeTrackedMinErrorComponentAttr] = {
    "time_tracked_min",
}


def check_api_v1_notes_list_time_tracked_min_error_component_attr(
    value: str,
) -> ApiV1NotesListTimeTrackedMinErrorComponentAttr:
    if value in API_V1_NOTES_LIST_TIME_TRACKED_MIN_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_LIST_TIME_TRACKED_MIN_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
