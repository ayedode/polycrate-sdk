from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateTargetWorkspacesErrorComponentAttr = Literal["target_workspaces"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_TARGET_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateTargetWorkspacesErrorComponentAttr
] = {
    "target_workspaces",
}


def check_api_v1_block_rollout_configs_archive_create_target_workspaces_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateTargetWorkspacesErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_TARGET_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_TARGET_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
