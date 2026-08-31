from typing import Literal

ApiV1NotesArchiveCreateAssignedToIdsINDEXErrorComponentCode = Literal[
    "invalid", "max_string_length", "null", "required"
]

API_V1_NOTES_ARCHIVE_CREATE_ASSIGNED_TO_IDS_INDEX_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesArchiveCreateAssignedToIdsINDEXErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "null",
    "required",
}


def check_api_v1_notes_archive_create_assigned_to_ids_index_error_component_code(
    value: str,
) -> ApiV1NotesArchiveCreateAssignedToIdsINDEXErrorComponentCode:
    if value in API_V1_NOTES_ARCHIVE_CREATE_ASSIGNED_TO_IDS_INDEX_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_ARCHIVE_CREATE_ASSIGNED_TO_IDS_INDEX_ERROR_COMPONENT_CODE_VALUES!r}"
    )
