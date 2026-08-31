from typing import Literal

ApiV1BlockRolloutConfigsPartialUpdateReconciliationTaskMetaErrorComponentCode = Literal["invalid"]

API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_RECONCILIATION_TASK_META_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsPartialUpdateReconciliationTaskMetaErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_block_rollout_configs_partial_update_reconciliation_task_meta_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsPartialUpdateReconciliationTaskMetaErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_RECONCILIATION_TASK_META_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_RECONCILIATION_TASK_META_ERROR_COMPONENT_CODE_VALUES!r}"
    )
