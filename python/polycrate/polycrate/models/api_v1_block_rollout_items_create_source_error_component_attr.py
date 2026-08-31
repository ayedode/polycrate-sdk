from typing import Literal

ApiV1BlockRolloutItemsCreateSourceErrorComponentAttr = Literal["source"]

API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_SOURCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsCreateSourceErrorComponentAttr
] = {
    "source",
}


def check_api_v1_block_rollout_items_create_source_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsCreateSourceErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_SOURCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_SOURCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
