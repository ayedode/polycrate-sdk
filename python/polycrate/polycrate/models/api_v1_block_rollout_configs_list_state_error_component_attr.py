from typing import Literal

ApiV1BlockRolloutConfigsListStateErrorComponentAttr = Literal["state"]

API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsListStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_block_rollout_configs_list_state_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsListStateErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
