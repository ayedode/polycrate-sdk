from typing import Literal

ApiV1WorkspacesListStateErrorComponentAttr = Literal["state"]

API_V1_WORKSPACES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1WorkspacesListStateErrorComponentAttr] = {
    "state",
}


def check_api_v1_workspaces_list_state_error_component_attr(value: str) -> ApiV1WorkspacesListStateErrorComponentAttr:
    if value in API_V1_WORKSPACES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
