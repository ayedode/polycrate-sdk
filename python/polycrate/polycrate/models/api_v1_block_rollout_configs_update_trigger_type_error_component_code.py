from typing import Literal

ApiV1BlockRolloutConfigsUpdateTriggerTypeErrorComponentCode = Literal["invalid_choice"]

API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_TRIGGER_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsUpdateTriggerTypeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_block_rollout_configs_update_trigger_type_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsUpdateTriggerTypeErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_TRIGGER_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_TRIGGER_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
