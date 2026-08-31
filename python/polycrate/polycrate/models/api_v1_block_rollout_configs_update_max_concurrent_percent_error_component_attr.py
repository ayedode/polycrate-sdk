from typing import Literal

ApiV1BlockRolloutConfigsUpdateMaxConcurrentPercentErrorComponentAttr = Literal["max_concurrent_percent"]

API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_MAX_CONCURRENT_PERCENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsUpdateMaxConcurrentPercentErrorComponentAttr
] = {
    "max_concurrent_percent",
}


def check_api_v1_block_rollout_configs_update_max_concurrent_percent_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsUpdateMaxConcurrentPercentErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_MAX_CONCURRENT_PERCENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_MAX_CONCURRENT_PERCENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
