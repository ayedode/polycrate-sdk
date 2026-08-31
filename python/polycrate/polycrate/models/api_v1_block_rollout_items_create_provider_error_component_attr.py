from typing import Literal

ApiV1BlockRolloutItemsCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_block_rollout_items_create_provider_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsCreateProviderErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
