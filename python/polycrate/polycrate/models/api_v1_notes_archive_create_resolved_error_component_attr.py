from typing import Literal

ApiV1NotesArchiveCreateResolvedErrorComponentAttr = Literal["resolved"]

API_V1_NOTES_ARCHIVE_CREATE_RESOLVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesArchiveCreateResolvedErrorComponentAttr
] = {
    "resolved",
}


def check_api_v1_notes_archive_create_resolved_error_component_attr(
    value: str,
) -> ApiV1NotesArchiveCreateResolvedErrorComponentAttr:
    if value in API_V1_NOTES_ARCHIVE_CREATE_RESOLVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_ARCHIVE_CREATE_RESOLVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
