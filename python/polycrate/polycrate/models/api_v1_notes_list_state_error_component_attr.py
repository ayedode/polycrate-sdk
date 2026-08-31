from typing import Literal

ApiV1NotesListStateErrorComponentAttr = Literal["state"]

API_V1_NOTES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesListStateErrorComponentAttr] = {
    "state",
}


def check_api_v1_notes_list_state_error_component_attr(value: str) -> ApiV1NotesListStateErrorComponentAttr:
    if value in API_V1_NOTES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
