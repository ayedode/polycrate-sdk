from typing import Literal

ApiV1BlockRolloutItemsListSource = Literal["manual", "scheduler"]

API_V1_BLOCK_ROLLOUT_ITEMS_LIST_SOURCE_VALUES: set[ApiV1BlockRolloutItemsListSource] = {
    "manual",
    "scheduler",
}


def check_api_v1_block_rollout_items_list_source(value: str) -> ApiV1BlockRolloutItemsListSource:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_LIST_SOURCE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_LIST_SOURCE_VALUES!r}")
