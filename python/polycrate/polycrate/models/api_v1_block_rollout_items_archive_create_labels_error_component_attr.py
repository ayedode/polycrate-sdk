from typing import Literal

ApiV1BlockRolloutItemsArchiveCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsArchiveCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_block_rollout_items_archive_create_labels_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsArchiveCreateLabelsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
