from typing import Literal

ApiV1BlockRolloutsArchiveCreateCompletedItemsErrorComponentAttr = Literal["completed_items"]

API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_COMPLETED_ITEMS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsArchiveCreateCompletedItemsErrorComponentAttr
] = {
    "completed_items",
}


def check_api_v1_block_rollouts_archive_create_completed_items_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsArchiveCreateCompletedItemsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_COMPLETED_ITEMS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_COMPLETED_ITEMS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
