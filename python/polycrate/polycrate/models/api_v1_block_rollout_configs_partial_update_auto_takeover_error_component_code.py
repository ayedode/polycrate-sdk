from typing import Literal

ApiV1BlockRolloutConfigsPartialUpdateAutoTakeoverErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_AUTO_TAKEOVER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsPartialUpdateAutoTakeoverErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollout_configs_partial_update_auto_takeover_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsPartialUpdateAutoTakeoverErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_AUTO_TAKEOVER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_AUTO_TAKEOVER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
