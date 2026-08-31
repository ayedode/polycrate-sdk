from typing import Literal

ApiV1NotesArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_NOTES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesArchiveCreateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_notes_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1NotesArchiveCreateNameErrorComponentAttr:
    if value in API_V1_NOTES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
