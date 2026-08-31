from typing import Literal

ApiV1BlockRolloutItemsArchiveCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsArchiveCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_block_rollout_items_archive_create_criticality_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsArchiveCreateCriticalityErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
