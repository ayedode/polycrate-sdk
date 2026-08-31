from typing import Literal

ApiV1NotesPartialUpdateContentErrorComponentAttr = Literal["content"]

API_V1_NOTES_PARTIAL_UPDATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesPartialUpdateContentErrorComponentAttr
] = {
    "content",
}


def check_api_v1_notes_partial_update_content_error_component_attr(
    value: str,
) -> ApiV1NotesPartialUpdateContentErrorComponentAttr:
    if value in API_V1_NOTES_PARTIAL_UPDATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_PARTIAL_UPDATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
