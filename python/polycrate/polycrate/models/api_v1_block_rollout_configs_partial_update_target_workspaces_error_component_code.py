from typing import Literal

ApiV1BlockRolloutConfigsPartialUpdateTargetWorkspacesErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "not_a_list", "null"
]

API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_TARGET_WORKSPACES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsPartialUpdateTargetWorkspacesErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "not_a_list",
    "null",
}


def check_api_v1_block_rollout_configs_partial_update_target_workspaces_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsPartialUpdateTargetWorkspacesErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_TARGET_WORKSPACES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_TARGET_WORKSPACES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
