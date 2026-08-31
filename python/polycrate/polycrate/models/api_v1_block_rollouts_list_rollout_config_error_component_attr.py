from typing import Literal

ApiV1BlockRolloutsListRolloutConfigErrorComponentAttr = Literal["rollout_config"]

API_V1_BLOCK_ROLLOUTS_LIST_ROLLOUT_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsListRolloutConfigErrorComponentAttr
] = {
    "rollout_config",
}


def check_api_v1_block_rollouts_list_rollout_config_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsListRolloutConfigErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_LIST_ROLLOUT_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_LIST_ROLLOUT_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
