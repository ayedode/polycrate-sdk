from typing import Literal

ApiV1BlockRolloutConfigsUpdateLastStateErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_LAST_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsUpdateLastStateErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_block_rollout_configs_update_last_state_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsUpdateLastStateErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_LAST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_LAST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
