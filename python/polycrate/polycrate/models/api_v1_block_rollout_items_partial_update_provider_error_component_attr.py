from typing import Literal

ApiV1BlockRolloutItemsPartialUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsPartialUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_block_rollout_items_partial_update_provider_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsPartialUpdateProviderErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
