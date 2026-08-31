from typing import Literal

ApiV1WorkspacesListPopErrorComponentAttr = Literal["pop"]

API_V1_WORKSPACES_LIST_POP_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1WorkspacesListPopErrorComponentAttr] = {
    "pop",
}


def check_api_v1_workspaces_list_pop_error_component_attr(value: str) -> ApiV1WorkspacesListPopErrorComponentAttr:
    if value in API_V1_WORKSPACES_LIST_POP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LIST_POP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
