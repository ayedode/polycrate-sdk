from typing import Literal

ApiV1WorkspacesDiscoverCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_WORKSPACES_DISCOVER_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesDiscoverCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_workspaces_discover_create_display_name_error_component_attr(
    value: str,
) -> ApiV1WorkspacesDiscoverCreateDisplayNameErrorComponentAttr:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
