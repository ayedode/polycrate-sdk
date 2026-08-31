from typing import Literal

ApiV1BlockRolloutsPartialUpdateStateErrorComponentAttr = Literal["state"]

API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsPartialUpdateStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_block_rollouts_partial_update_state_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsPartialUpdateStateErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
