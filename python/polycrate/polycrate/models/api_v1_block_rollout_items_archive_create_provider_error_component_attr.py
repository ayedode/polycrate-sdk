from typing import Literal

ApiV1BlockRolloutItemsArchiveCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsArchiveCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_block_rollout_items_archive_create_provider_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsArchiveCreateProviderErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
