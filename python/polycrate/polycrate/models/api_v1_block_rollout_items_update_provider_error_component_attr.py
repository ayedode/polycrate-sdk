from typing import Literal

ApiV1BlockRolloutItemsUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_block_rollout_items_update_provider_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsUpdateProviderErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
