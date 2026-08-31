from typing import Literal

ApiV1NotesUpdateTrackedAtErrorComponentAttr = Literal["tracked_at"]

API_V1_NOTES_UPDATE_TRACKED_AT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesUpdateTrackedAtErrorComponentAttr] = {
    "tracked_at",
}


def check_api_v1_notes_update_tracked_at_error_component_attr(
    value: str,
) -> ApiV1NotesUpdateTrackedAtErrorComponentAttr:
    if value in API_V1_NOTES_UPDATE_TRACKED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_UPDATE_TRACKED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
