from typing import Literal

ApiV1BlockRolloutItemsUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_block_rollout_items_update_kind_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsUpdateKindErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
