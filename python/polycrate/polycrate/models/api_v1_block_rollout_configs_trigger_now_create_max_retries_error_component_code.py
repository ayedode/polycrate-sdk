from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateMaxRetriesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_MAX_RETRIES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateMaxRetriesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_block_rollout_configs_trigger_now_create_max_retries_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateMaxRetriesErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_MAX_RETRIES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_MAX_RETRIES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
