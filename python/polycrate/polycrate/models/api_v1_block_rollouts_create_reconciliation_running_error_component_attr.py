from typing import Literal

ApiV1BlockRolloutsCreateReconciliationRunningErrorComponentAttr = Literal["reconciliation_running"]

API_V1_BLOCK_ROLLOUTS_CREATE_RECONCILIATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsCreateReconciliationRunningErrorComponentAttr
] = {
    "reconciliation_running",
}


def check_api_v1_block_rollouts_create_reconciliation_running_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsCreateReconciliationRunningErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_RECONCILIATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_RECONCILIATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
