from typing import Literal

ApiV1NotesPartialUpdateStructuredContentErrorComponentAttr = Literal["structured_content"]

API_V1_NOTES_PARTIAL_UPDATE_STRUCTURED_CONTENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesPartialUpdateStructuredContentErrorComponentAttr
] = {
    "structured_content",
}


def check_api_v1_notes_partial_update_structured_content_error_component_attr(
    value: str,
) -> ApiV1NotesPartialUpdateStructuredContentErrorComponentAttr:
    if value in API_V1_NOTES_PARTIAL_UPDATE_STRUCTURED_CONTENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_PARTIAL_UPDATE_STRUCTURED_CONTENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
