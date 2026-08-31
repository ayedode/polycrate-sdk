from typing import Literal

ApiV1BlockRolloutItemsArchiveCreateSourceErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_SOURCE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsArchiveCreateSourceErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_block_rollout_items_archive_create_source_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsArchiveCreateSourceErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_SOURCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_SOURCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
