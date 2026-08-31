from typing import Literal

ApiV1BlocksListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_BLOCKS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksListWorkspacesErrorComponentAttr] = {
    "workspaces",
}


def check_api_v1_blocks_list_workspaces_error_component_attr(value: str) -> ApiV1BlocksListWorkspacesErrorComponentAttr:
    if value in API_V1_BLOCKS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
