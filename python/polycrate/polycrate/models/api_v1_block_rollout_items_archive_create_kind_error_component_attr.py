from typing import Literal

ApiV1BlockRolloutItemsArchiveCreateKindErrorComponentAttr = Literal["kind"]

API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsArchiveCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_block_rollout_items_archive_create_kind_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsArchiveCreateKindErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
