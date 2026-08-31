from typing import Literal

ApiV1BlockRolloutsListRolloutConfigErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_BLOCK_ROLLOUTS_LIST_ROLLOUT_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsListRolloutConfigErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_block_rollouts_list_rollout_config_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsListRolloutConfigErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_LIST_ROLLOUT_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_LIST_ROLLOUT_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
