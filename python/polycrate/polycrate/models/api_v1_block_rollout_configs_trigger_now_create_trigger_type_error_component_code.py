from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateTriggerTypeErrorComponentCode = Literal["invalid_choice"]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_TRIGGER_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateTriggerTypeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_block_rollout_configs_trigger_now_create_trigger_type_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateTriggerTypeErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_TRIGGER_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_TRIGGER_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
