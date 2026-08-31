from typing import Literal

ApiV1NotesListAssignedToErrorComponentAttr = Literal["assigned_to"]

API_V1_NOTES_LIST_ASSIGNED_TO_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesListAssignedToErrorComponentAttr] = {
    "assigned_to",
}


def check_api_v1_notes_list_assigned_to_error_component_attr(value: str) -> ApiV1NotesListAssignedToErrorComponentAttr:
    if value in API_V1_NOTES_LIST_ASSIGNED_TO_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_LIST_ASSIGNED_TO_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
