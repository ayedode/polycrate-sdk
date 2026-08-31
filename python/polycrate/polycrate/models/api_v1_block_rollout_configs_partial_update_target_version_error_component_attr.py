from typing import Literal

ApiV1BlockRolloutConfigsPartialUpdateTargetVersionErrorComponentAttr = Literal["target_version"]

API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_TARGET_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsPartialUpdateTargetVersionErrorComponentAttr
] = {
    "target_version",
}


def check_api_v1_block_rollout_configs_partial_update_target_version_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsPartialUpdateTargetVersionErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_TARGET_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_TARGET_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
