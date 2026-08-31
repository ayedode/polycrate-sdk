from typing import Literal

ApiV1RegionsListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_REGIONS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1RegionsListWorkspacesErrorComponentAttr] = {
    "workspaces",
}


def check_api_v1_regions_list_workspaces_error_component_attr(
    value: str,
) -> ApiV1RegionsListWorkspacesErrorComponentAttr:
    if value in API_V1_REGIONS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
