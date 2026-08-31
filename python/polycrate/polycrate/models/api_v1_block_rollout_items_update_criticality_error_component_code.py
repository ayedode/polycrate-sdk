from typing import Literal

ApiV1BlockRolloutItemsUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_block_rollout_items_update_criticality_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsUpdateCriticalityErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
