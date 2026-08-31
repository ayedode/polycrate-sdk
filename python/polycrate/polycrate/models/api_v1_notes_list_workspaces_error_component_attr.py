from typing import Literal

ApiV1NotesListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_NOTES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesListWorkspacesErrorComponentAttr] = {
    "workspaces",
}


def check_api_v1_notes_list_workspaces_error_component_attr(value: str) -> ApiV1NotesListWorkspacesErrorComponentAttr:
    if value in API_V1_NOTES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
