from typing import Literal

ApiV1BlockRolloutItemsUpdateReconciliationTaskIdErrorComponentAttr = Literal["reconciliation_task_id"]

API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_RECONCILIATION_TASK_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsUpdateReconciliationTaskIdErrorComponentAttr
] = {
    "reconciliation_task_id",
}


def check_api_v1_block_rollout_items_update_reconciliation_task_id_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsUpdateReconciliationTaskIdErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_RECONCILIATION_TASK_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_RECONCILIATION_TASK_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
