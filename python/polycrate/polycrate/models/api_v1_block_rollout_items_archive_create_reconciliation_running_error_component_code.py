from typing import Literal

ApiV1BlockRolloutItemsArchiveCreateReconciliationRunningErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_RECONCILIATION_RUNNING_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsArchiveCreateReconciliationRunningErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollout_items_archive_create_reconciliation_running_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsArchiveCreateReconciliationRunningErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_RECONCILIATION_RUNNING_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_RECONCILIATION_RUNNING_ERROR_COMPONENT_CODE_VALUES!r}"
    )
