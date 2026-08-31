from typing import Literal

ApiV1NotesUpdateAssignedToIdsINDEXErrorComponentAttr = Literal["assigned_to_ids.INDEX"]

API_V1_NOTES_UPDATE_ASSIGNED_TO_IDS_INDEX_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesUpdateAssignedToIdsINDEXErrorComponentAttr
] = {
    "assigned_to_ids.INDEX",
}


def check_api_v1_notes_update_assigned_to_ids_index_error_component_attr(
    value: str,
) -> ApiV1NotesUpdateAssignedToIdsINDEXErrorComponentAttr:
    if value in API_V1_NOTES_UPDATE_ASSIGNED_TO_IDS_INDEX_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_UPDATE_ASSIGNED_TO_IDS_INDEX_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
