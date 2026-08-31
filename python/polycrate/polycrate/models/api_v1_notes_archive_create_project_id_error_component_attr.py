from typing import Literal

ApiV1NotesArchiveCreateProjectIdErrorComponentAttr = Literal["project_id"]

API_V1_NOTES_ARCHIVE_CREATE_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesArchiveCreateProjectIdErrorComponentAttr
] = {
    "project_id",
}


def check_api_v1_notes_archive_create_project_id_error_component_attr(
    value: str,
) -> ApiV1NotesArchiveCreateProjectIdErrorComponentAttr:
    if value in API_V1_NOTES_ARCHIVE_CREATE_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_ARCHIVE_CREATE_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
