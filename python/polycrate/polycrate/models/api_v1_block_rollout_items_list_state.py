from typing import Literal

ApiV1BlockRolloutItemsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_BLOCK_ROLLOUT_ITEMS_LIST_STATE_VALUES: set[ApiV1BlockRolloutItemsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_block_rollout_items_list_state(value: str) -> ApiV1BlockRolloutItemsListState:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_LIST_STATE_VALUES!r}")
