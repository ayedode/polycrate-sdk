from typing import Literal

ApiV1BlockRolloutItemsCreateReasonErrorComponentAttr = Literal["reason"]

API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsCreateReasonErrorComponentAttr
] = {
    "reason",
}


def check_api_v1_block_rollout_items_create_reason_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsCreateReasonErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
