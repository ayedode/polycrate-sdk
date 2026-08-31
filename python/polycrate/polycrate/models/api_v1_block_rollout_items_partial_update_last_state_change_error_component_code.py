from typing import Literal

ApiV1BlockRolloutItemsPartialUpdateLastStateChangeErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_LAST_STATE_CHANGE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsPartialUpdateLastStateChangeErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_block_rollout_items_partial_update_last_state_change_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsPartialUpdateLastStateChangeErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_LAST_STATE_CHANGE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_LAST_STATE_CHANGE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
