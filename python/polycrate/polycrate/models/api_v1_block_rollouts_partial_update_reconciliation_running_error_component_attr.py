from typing import Literal

ApiV1BlockRolloutsPartialUpdateReconciliationRunningErrorComponentAttr = Literal["reconciliation_running"]

API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_RECONCILIATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsPartialUpdateReconciliationRunningErrorComponentAttr
] = {
    "reconciliation_running",
}


def check_api_v1_block_rollouts_partial_update_reconciliation_running_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsPartialUpdateReconciliationRunningErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_RECONCILIATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_RECONCILIATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
