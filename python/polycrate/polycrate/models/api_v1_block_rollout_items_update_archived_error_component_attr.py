from typing import Literal

ApiV1BlockRolloutItemsUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_block_rollout_items_update_archived_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsUpdateArchivedErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
