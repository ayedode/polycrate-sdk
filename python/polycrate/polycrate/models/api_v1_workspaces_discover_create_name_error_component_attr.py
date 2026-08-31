from typing import Literal

ApiV1WorkspacesDiscoverCreateNameErrorComponentAttr = Literal["name"]

API_V1_WORKSPACES_DISCOVER_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesDiscoverCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_workspaces_discover_create_name_error_component_attr(
    value: str,
) -> ApiV1WorkspacesDiscoverCreateNameErrorComponentAttr:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
