from typing import Literal

ApiV1BlockRolloutItemsArchiveCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsArchiveCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_block_rollout_items_archive_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsArchiveCreateDebugModeErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
