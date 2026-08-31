from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationTaskIdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_RECONCILIATION_TASK_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationTaskIdErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_block_rollout_configs_trigger_now_create_reconciliation_task_id_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationTaskIdErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_RECONCILIATION_TASK_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_RECONCILIATION_TASK_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
