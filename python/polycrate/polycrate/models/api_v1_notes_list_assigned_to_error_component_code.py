from typing import Literal

ApiV1NotesListAssignedToErrorComponentCode = Literal["invalid_choice", "invalid_list", "invalid_pk_value"]

API_V1_NOTES_LIST_ASSIGNED_TO_ERROR_COMPONENT_CODE_VALUES: set[ApiV1NotesListAssignedToErrorComponentCode] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_notes_list_assigned_to_error_component_code(value: str) -> ApiV1NotesListAssignedToErrorComponentCode:
    if value in API_V1_NOTES_LIST_ASSIGNED_TO_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_LIST_ASSIGNED_TO_ERROR_COMPONENT_CODE_VALUES!r}"
    )
