from typing import Literal

ApiV1NotesCreateContentErrorComponentAttr = Literal["content"]

API_V1_NOTES_CREATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesCreateContentErrorComponentAttr] = {
    "content",
}


def check_api_v1_notes_create_content_error_component_attr(value: str) -> ApiV1NotesCreateContentErrorComponentAttr:
    if value in API_V1_NOTES_CREATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_CREATE_CONTENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
