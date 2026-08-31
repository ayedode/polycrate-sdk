from typing import Literal

ApiV1BlockRolloutItemsArchiveCreateRolloutErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_ROLLOUT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsArchiveCreateRolloutErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_block_rollout_items_archive_create_rollout_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsArchiveCreateRolloutErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_ROLLOUT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_ROLLOUT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
