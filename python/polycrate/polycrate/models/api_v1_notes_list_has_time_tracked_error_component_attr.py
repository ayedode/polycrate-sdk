from typing import Literal

ApiV1NotesListHasTimeTrackedErrorComponentAttr = Literal["has_time_tracked"]

API_V1_NOTES_LIST_HAS_TIME_TRACKED_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesListHasTimeTrackedErrorComponentAttr] = {
    "has_time_tracked",
}


def check_api_v1_notes_list_has_time_tracked_error_component_attr(
    value: str,
) -> ApiV1NotesListHasTimeTrackedErrorComponentAttr:
    if value in API_V1_NOTES_LIST_HAS_TIME_TRACKED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_LIST_HAS_TIME_TRACKED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
