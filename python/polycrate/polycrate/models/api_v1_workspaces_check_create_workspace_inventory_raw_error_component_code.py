from typing import Literal

ApiV1WorkspacesCheckCreateWorkspaceInventoryRawErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_WORKSPACES_CHECK_CREATE_WORKSPACE_INVENTORY_RAW_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesCheckCreateWorkspaceInventoryRawErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_workspaces_check_create_workspace_inventory_raw_error_component_code(
    value: str,
) -> ApiV1WorkspacesCheckCreateWorkspaceInventoryRawErrorComponentCode:
    if value in API_V1_WORKSPACES_CHECK_CREATE_WORKSPACE_INVENTORY_RAW_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_WORKSPACE_INVENTORY_RAW_ERROR_COMPONENT_CODE_VALUES!r}"
    )
