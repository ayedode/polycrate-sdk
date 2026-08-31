from typing import Literal

ApiV1BlockRolloutItemsArchiveCreateStateReasonErrorComponentAttr = Literal["state_reason"]

API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_STATE_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsArchiveCreateStateReasonErrorComponentAttr
] = {
    "state_reason",
}


def check_api_v1_block_rollout_items_archive_create_state_reason_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsArchiveCreateStateReasonErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_STATE_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_STATE_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
