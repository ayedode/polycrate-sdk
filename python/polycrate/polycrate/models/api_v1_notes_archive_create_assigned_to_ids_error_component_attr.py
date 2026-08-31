from typing import Literal

ApiV1NotesArchiveCreateAssignedToIdsErrorComponentAttr = Literal["assigned_to_ids"]

API_V1_NOTES_ARCHIVE_CREATE_ASSIGNED_TO_IDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesArchiveCreateAssignedToIdsErrorComponentAttr
] = {
    "assigned_to_ids",
}


def check_api_v1_notes_archive_create_assigned_to_ids_error_component_attr(
    value: str,
) -> ApiV1NotesArchiveCreateAssignedToIdsErrorComponentAttr:
    if value in API_V1_NOTES_ARCHIVE_CREATE_ASSIGNED_TO_IDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_ARCHIVE_CREATE_ASSIGNED_TO_IDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
