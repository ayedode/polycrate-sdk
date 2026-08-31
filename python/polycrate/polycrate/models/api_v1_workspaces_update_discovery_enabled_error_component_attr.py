from typing import Literal

ApiV1WorkspacesUpdateDiscoveryEnabledErrorComponentAttr = Literal["discovery_enabled"]

API_V1_WORKSPACES_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateDiscoveryEnabledErrorComponentAttr
] = {
    "discovery_enabled",
}


def check_api_v1_workspaces_update_discovery_enabled_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateDiscoveryEnabledErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
