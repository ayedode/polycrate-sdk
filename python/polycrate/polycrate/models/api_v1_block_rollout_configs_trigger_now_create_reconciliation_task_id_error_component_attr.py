from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationTaskIdErrorComponentAttr = Literal["reconciliation_task_id"]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_RECONCILIATION_TASK_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationTaskIdErrorComponentAttr
] = {
    "reconciliation_task_id",
}


def check_api_v1_block_rollout_configs_trigger_now_create_reconciliation_task_id_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationTaskIdErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_RECONCILIATION_TASK_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_RECONCILIATION_TASK_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
