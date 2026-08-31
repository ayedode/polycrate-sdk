from typing import Literal

ApiV1NotesArchiveCreateStructuredContentErrorComponentAttr = Literal["structured_content"]

API_V1_NOTES_ARCHIVE_CREATE_STRUCTURED_CONTENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesArchiveCreateStructuredContentErrorComponentAttr
] = {
    "structured_content",
}


def check_api_v1_notes_archive_create_structured_content_error_component_attr(
    value: str,
) -> ApiV1NotesArchiveCreateStructuredContentErrorComponentAttr:
    if value in API_V1_NOTES_ARCHIVE_CREATE_STRUCTURED_CONTENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_ARCHIVE_CREATE_STRUCTURED_CONTENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
