from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateReconciliationRunningErrorComponentAttr = Literal["reconciliation_running"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_RECONCILIATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateReconciliationRunningErrorComponentAttr
] = {
    "reconciliation_running",
}


def check_api_v1_block_rollout_configs_archive_create_reconciliation_running_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateReconciliationRunningErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_RECONCILIATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_RECONCILIATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
