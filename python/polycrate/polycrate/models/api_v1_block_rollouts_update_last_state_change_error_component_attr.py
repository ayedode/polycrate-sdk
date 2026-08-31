from typing import Literal

ApiV1BlockRolloutsUpdateLastStateChangeErrorComponentAttr = Literal["last_state_change"]

API_V1_BLOCK_ROLLOUTS_UPDATE_LAST_STATE_CHANGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsUpdateLastStateChangeErrorComponentAttr
] = {
    "last_state_change",
}


def check_api_v1_block_rollouts_update_last_state_change_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsUpdateLastStateChangeErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_UPDATE_LAST_STATE_CHANGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_UPDATE_LAST_STATE_CHANGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
