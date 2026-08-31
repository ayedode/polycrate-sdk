from typing import Literal

ApiV1BlockRolloutItemsCreateReconciliationTaskMetaErrorComponentAttr = Literal["reconciliation_task_meta"]

API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_RECONCILIATION_TASK_META_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsCreateReconciliationTaskMetaErrorComponentAttr
] = {
    "reconciliation_task_meta",
}


def check_api_v1_block_rollout_items_create_reconciliation_task_meta_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsCreateReconciliationTaskMetaErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_RECONCILIATION_TASK_META_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_RECONCILIATION_TASK_META_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
