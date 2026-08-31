from typing import Literal

ApiV1BlockRolloutsCreateReconciliationTaskMetaErrorComponentCode = Literal["invalid"]

API_V1_BLOCK_ROLLOUTS_CREATE_RECONCILIATION_TASK_META_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsCreateReconciliationTaskMetaErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_block_rollouts_create_reconciliation_task_meta_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsCreateReconciliationTaskMetaErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_RECONCILIATION_TASK_META_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_RECONCILIATION_TASK_META_ERROR_COMPONENT_CODE_VALUES!r}"
    )
