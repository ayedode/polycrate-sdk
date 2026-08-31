from typing import Literal

ApiV1WorkspacesCheckCreateWorkspaceInventoryRawErrorComponentAttr = Literal["workspace_inventory_raw"]

API_V1_WORKSPACES_CHECK_CREATE_WORKSPACE_INVENTORY_RAW_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCheckCreateWorkspaceInventoryRawErrorComponentAttr
] = {
    "workspace_inventory_raw",
}


def check_api_v1_workspaces_check_create_workspace_inventory_raw_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCheckCreateWorkspaceInventoryRawErrorComponentAttr:
    if value in API_V1_WORKSPACES_CHECK_CREATE_WORKSPACE_INVENTORY_RAW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_WORKSPACE_INVENTORY_RAW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
