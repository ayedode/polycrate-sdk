from typing import Literal

ApiV1BlockRolloutConfigsCreateMaxConcurrentPercentErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_MAX_CONCURRENT_PERCENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsCreateMaxConcurrentPercentErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_block_rollout_configs_create_max_concurrent_percent_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateMaxConcurrentPercentErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_MAX_CONCURRENT_PERCENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_MAX_CONCURRENT_PERCENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
