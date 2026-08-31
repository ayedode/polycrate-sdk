from typing import Literal

ApiV1BlockRolloutItemsCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_block_rollout_items_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsCreateProviderIdErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
