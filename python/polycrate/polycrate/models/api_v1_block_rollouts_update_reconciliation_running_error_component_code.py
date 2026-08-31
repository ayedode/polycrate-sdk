from typing import Literal

ApiV1BlockRolloutsUpdateReconciliationRunningErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUTS_UPDATE_RECONCILIATION_RUNNING_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsUpdateReconciliationRunningErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollouts_update_reconciliation_running_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsUpdateReconciliationRunningErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_UPDATE_RECONCILIATION_RUNNING_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_UPDATE_RECONCILIATION_RUNNING_ERROR_COMPONENT_CODE_VALUES!r}"
    )
