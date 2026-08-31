from typing import Literal

ApiV1NotesUpdateAssignedToIdsErrorComponentCode = Literal["not_a_list", "null"]

API_V1_NOTES_UPDATE_ASSIGNED_TO_IDS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesUpdateAssignedToIdsErrorComponentCode
] = {
    "not_a_list",
    "null",
}


def check_api_v1_notes_update_assigned_to_ids_error_component_code(
    value: str,
) -> ApiV1NotesUpdateAssignedToIdsErrorComponentCode:
    if value in API_V1_NOTES_UPDATE_ASSIGNED_TO_IDS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_UPDATE_ASSIGNED_TO_IDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
