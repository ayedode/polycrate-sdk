from typing import Literal

ApiV1BlockRolloutConfigsCreateFailureThresholdPercentErrorComponentAttr = Literal["failure_threshold_percent"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_FAILURE_THRESHOLD_PERCENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsCreateFailureThresholdPercentErrorComponentAttr
] = {
    "failure_threshold_percent",
}


def check_api_v1_block_rollout_configs_create_failure_threshold_percent_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateFailureThresholdPercentErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_FAILURE_THRESHOLD_PERCENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_FAILURE_THRESHOLD_PERCENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
