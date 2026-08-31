from typing import Literal

ApiV1BlockRolloutItemsPartialUpdateReconciliationTaskMetaErrorComponentAttr = Literal["reconciliation_task_meta"]

API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_RECONCILIATION_TASK_META_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsPartialUpdateReconciliationTaskMetaErrorComponentAttr
] = {
    "reconciliation_task_meta",
}


def check_api_v1_block_rollout_items_partial_update_reconciliation_task_meta_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsPartialUpdateReconciliationTaskMetaErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_RECONCILIATION_TASK_META_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_RECONCILIATION_TASK_META_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
