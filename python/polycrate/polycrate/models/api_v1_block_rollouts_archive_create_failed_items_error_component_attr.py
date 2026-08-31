from typing import Literal

ApiV1BlockRolloutsArchiveCreateFailedItemsErrorComponentAttr = Literal["failed_items"]

API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_FAILED_ITEMS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsArchiveCreateFailedItemsErrorComponentAttr
] = {
    "failed_items",
}


def check_api_v1_block_rollouts_archive_create_failed_items_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsArchiveCreateFailedItemsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_FAILED_ITEMS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_FAILED_ITEMS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
