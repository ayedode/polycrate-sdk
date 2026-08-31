from typing import Literal

ApiV1NotesListProjectErrorComponentAttr = Literal["project"]

API_V1_NOTES_LIST_PROJECT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesListProjectErrorComponentAttr] = {
    "project",
}


def check_api_v1_notes_list_project_error_component_attr(value: str) -> ApiV1NotesListProjectErrorComponentAttr:
    if value in API_V1_NOTES_LIST_PROJECT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_LIST_PROJECT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
