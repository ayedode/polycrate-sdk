from typing import Literal

ApiV1BlockRolloutConfigsCreateTargetWorkspacesErrorComponentAttr = Literal["target_workspaces"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_TARGET_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsCreateTargetWorkspacesErrorComponentAttr
] = {
    "target_workspaces",
}


def check_api_v1_block_rollout_configs_create_target_workspaces_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateTargetWorkspacesErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_TARGET_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_TARGET_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
