from typing import Literal

ApiV1BlockRolloutConfigsUpdateTargetVersionErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_TARGET_VERSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsUpdateTargetVersionErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_block_rollout_configs_update_target_version_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsUpdateTargetVersionErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_TARGET_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_TARGET_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
