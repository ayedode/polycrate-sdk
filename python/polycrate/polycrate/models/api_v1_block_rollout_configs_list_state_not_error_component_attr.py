from typing import Literal

ApiV1BlockRolloutConfigsListStateNotErrorComponentAttr = Literal["state_not"]

API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsListStateNotErrorComponentAttr
] = {
    "state_not",
}


def check_api_v1_block_rollout_configs_list_state_not_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsListStateNotErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
