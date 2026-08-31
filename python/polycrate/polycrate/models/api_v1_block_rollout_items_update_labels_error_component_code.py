from typing import Literal

ApiV1BlockRolloutItemsUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_block_rollout_items_update_labels_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsUpdateLabelsErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
