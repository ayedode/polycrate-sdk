from typing import Literal

ApiV1BlockRolloutItemsUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_block_rollout_items_update_annotations_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsUpdateAnnotationsErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
