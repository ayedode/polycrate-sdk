from typing import Literal

ApiV1BlockRolloutItemsArchiveCreateBlockErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "null", "required"
]

API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_BLOCK_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsArchiveCreateBlockErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_block_rollout_items_archive_create_block_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsArchiveCreateBlockErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_BLOCK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_BLOCK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
