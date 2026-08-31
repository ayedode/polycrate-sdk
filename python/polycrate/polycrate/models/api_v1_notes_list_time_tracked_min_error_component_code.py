from typing import Literal

ApiV1NotesListTimeTrackedMinErrorComponentCode = Literal["invalid", "max_value"]

API_V1_NOTES_LIST_TIME_TRACKED_MIN_ERROR_COMPONENT_CODE_VALUES: set[ApiV1NotesListTimeTrackedMinErrorComponentCode] = {
    "invalid",
    "max_value",
}


def check_api_v1_notes_list_time_tracked_min_error_component_code(
    value: str,
) -> ApiV1NotesListTimeTrackedMinErrorComponentCode:
    if value in API_V1_NOTES_LIST_TIME_TRACKED_MIN_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_LIST_TIME_TRACKED_MIN_ERROR_COMPONENT_CODE_VALUES!r}"
    )
