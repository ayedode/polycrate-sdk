from typing import Literal

ApiV1BlockRolloutsListStateErrorComponentAttr = Literal["state"]

API_V1_BLOCK_ROLLOUTS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlockRolloutsListStateErrorComponentAttr] = {
    "state",
}


def check_api_v1_block_rollouts_list_state_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsListStateErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
