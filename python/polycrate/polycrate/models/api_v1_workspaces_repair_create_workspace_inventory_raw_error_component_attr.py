from typing import Literal

ApiV1WorkspacesRepairCreateWorkspaceInventoryRawErrorComponentAttr = Literal["workspace_inventory_raw"]

API_V1_WORKSPACES_REPAIR_CREATE_WORKSPACE_INVENTORY_RAW_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRepairCreateWorkspaceInventoryRawErrorComponentAttr
] = {
    "workspace_inventory_raw",
}


def check_api_v1_workspaces_repair_create_workspace_inventory_raw_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRepairCreateWorkspaceInventoryRawErrorComponentAttr:
    if value in API_V1_WORKSPACES_REPAIR_CREATE_WORKSPACE_INVENTORY_RAW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_REPAIR_CREATE_WORKSPACE_INVENTORY_RAW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
