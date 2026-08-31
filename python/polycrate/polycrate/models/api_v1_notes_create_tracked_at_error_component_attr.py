from typing import Literal

ApiV1NotesCreateTrackedAtErrorComponentAttr = Literal["tracked_at"]

API_V1_NOTES_CREATE_TRACKED_AT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesCreateTrackedAtErrorComponentAttr] = {
    "tracked_at",
}


def check_api_v1_notes_create_tracked_at_error_component_attr(
    value: str,
) -> ApiV1NotesCreateTrackedAtErrorComponentAttr:
    if value in API_V1_NOTES_CREATE_TRACKED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_CREATE_TRACKED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
