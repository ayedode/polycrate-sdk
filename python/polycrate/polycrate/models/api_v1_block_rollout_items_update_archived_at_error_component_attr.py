from typing import Literal

ApiV1BlockRolloutItemsUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_block_rollout_items_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
