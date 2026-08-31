from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_workspaces_run_discovery_create_display_name_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateDisplayNameErrorComponentAttr:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
