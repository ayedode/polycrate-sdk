from typing import Literal

ApiV1BlockRolloutItemsPartialUpdateSourceErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_SOURCE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsPartialUpdateSourceErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_block_rollout_items_partial_update_source_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsPartialUpdateSourceErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_SOURCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_SOURCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
