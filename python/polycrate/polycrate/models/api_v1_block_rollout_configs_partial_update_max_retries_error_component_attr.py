from typing import Literal

ApiV1BlockRolloutConfigsPartialUpdateMaxRetriesErrorComponentAttr = Literal["max_retries"]

API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_MAX_RETRIES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsPartialUpdateMaxRetriesErrorComponentAttr
] = {
    "max_retries",
}


def check_api_v1_block_rollout_configs_partial_update_max_retries_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsPartialUpdateMaxRetriesErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_MAX_RETRIES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_MAX_RETRIES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
