from typing import Literal

ApiV1BlockRolloutsPartialUpdateStateReasonErrorComponentAttr = Literal["state_reason"]

API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_STATE_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsPartialUpdateStateReasonErrorComponentAttr
] = {
    "state_reason",
}


def check_api_v1_block_rollouts_partial_update_state_reason_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsPartialUpdateStateReasonErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_STATE_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_STATE_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
