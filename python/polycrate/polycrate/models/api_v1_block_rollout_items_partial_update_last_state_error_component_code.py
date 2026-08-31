from typing import Literal

ApiV1BlockRolloutItemsPartialUpdateLastStateErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_LAST_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsPartialUpdateLastStateErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_block_rollout_items_partial_update_last_state_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsPartialUpdateLastStateErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_LAST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_LAST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
