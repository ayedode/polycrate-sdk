from typing import Literal

ApiV1BlockRolloutConfigsCreateMaxRetriesErrorComponentAttr = Literal["max_retries"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_MAX_RETRIES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsCreateMaxRetriesErrorComponentAttr
] = {
    "max_retries",
}


def check_api_v1_block_rollout_configs_create_max_retries_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateMaxRetriesErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_MAX_RETRIES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_MAX_RETRIES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
