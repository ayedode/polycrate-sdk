from typing import Literal

ApiV1BlockRolloutItemsPartialUpdateStateReasonErrorComponentAttr = Literal["state_reason"]

API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_STATE_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsPartialUpdateStateReasonErrorComponentAttr
] = {
    "state_reason",
}


def check_api_v1_block_rollout_items_partial_update_state_reason_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsPartialUpdateStateReasonErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_STATE_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_STATE_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
