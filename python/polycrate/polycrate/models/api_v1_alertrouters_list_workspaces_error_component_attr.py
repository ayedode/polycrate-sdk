from typing import Literal

ApiV1AlertroutersListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_ALERTROUTERS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersListWorkspacesErrorComponentAttr
] = {
    "workspaces",
}


def check_api_v1_alertrouters_list_workspaces_error_component_attr(
    value: str,
) -> ApiV1AlertroutersListWorkspacesErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
