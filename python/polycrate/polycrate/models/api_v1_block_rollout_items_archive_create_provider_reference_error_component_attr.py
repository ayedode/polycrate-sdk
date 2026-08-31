from typing import Literal

ApiV1BlockRolloutItemsArchiveCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsArchiveCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_block_rollout_items_archive_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsArchiveCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
