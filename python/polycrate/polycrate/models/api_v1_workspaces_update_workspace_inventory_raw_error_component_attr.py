from typing import Literal

ApiV1WorkspacesUpdateWorkspaceInventoryRawErrorComponentAttr = Literal["workspace_inventory_raw"]

API_V1_WORKSPACES_UPDATE_WORKSPACE_INVENTORY_RAW_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateWorkspaceInventoryRawErrorComponentAttr
] = {
    "workspace_inventory_raw",
}


def check_api_v1_workspaces_update_workspace_inventory_raw_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateWorkspaceInventoryRawErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_WORKSPACE_INVENTORY_RAW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_WORKSPACE_INVENTORY_RAW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
