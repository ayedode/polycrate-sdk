from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateKindErrorComponentCode = Literal["invalid_choice", "null", "required"]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
    "required",
}


def check_api_v1_block_rollout_configs_trigger_now_create_kind_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateKindErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
