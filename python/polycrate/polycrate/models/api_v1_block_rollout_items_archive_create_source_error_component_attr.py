from typing import Literal

ApiV1BlockRolloutItemsArchiveCreateSourceErrorComponentAttr = Literal["source"]

API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_SOURCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsArchiveCreateSourceErrorComponentAttr
] = {
    "source",
}


def check_api_v1_block_rollout_items_archive_create_source_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsArchiveCreateSourceErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_SOURCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_SOURCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
