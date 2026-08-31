from typing import Literal

ApiV1BlockRolloutConfigsUpdateFailureThresholdPercentErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_FAILURE_THRESHOLD_PERCENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsUpdateFailureThresholdPercentErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_block_rollout_configs_update_failure_threshold_percent_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsUpdateFailureThresholdPercentErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_FAILURE_THRESHOLD_PERCENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_FAILURE_THRESHOLD_PERCENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
