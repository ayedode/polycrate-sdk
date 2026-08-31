from typing import Literal

ApiV1NotesCreateAssignedToIdsINDEXErrorComponentAttr = Literal["assigned_to_ids.INDEX"]

API_V1_NOTES_CREATE_ASSIGNED_TO_IDS_INDEX_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesCreateAssignedToIdsINDEXErrorComponentAttr
] = {
    "assigned_to_ids.INDEX",
}


def check_api_v1_notes_create_assigned_to_ids_index_error_component_attr(
    value: str,
) -> ApiV1NotesCreateAssignedToIdsINDEXErrorComponentAttr:
    if value in API_V1_NOTES_CREATE_ASSIGNED_TO_IDS_INDEX_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_CREATE_ASSIGNED_TO_IDS_INDEX_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
