from typing import Literal

ApiV1BlockRolloutItemsArchiveCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsArchiveCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_block_rollout_items_archive_create_annotations_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsArchiveCreateAnnotationsErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
