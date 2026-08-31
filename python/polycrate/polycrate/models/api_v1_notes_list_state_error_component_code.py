from typing import Literal

ApiV1NotesListStateErrorComponentCode = Literal["invalid_choice"]

API_V1_NOTES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1NotesListStateErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_notes_list_state_error_component_code(value: str) -> ApiV1NotesListStateErrorComponentCode:
    if value in API_V1_NOTES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
