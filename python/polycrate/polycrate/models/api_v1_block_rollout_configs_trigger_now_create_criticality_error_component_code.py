from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_block_rollout_configs_trigger_now_create_criticality_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateCriticalityErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
