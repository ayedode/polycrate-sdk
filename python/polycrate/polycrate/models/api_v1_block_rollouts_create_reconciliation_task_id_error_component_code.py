from typing import Literal

ApiV1BlockRolloutsCreateReconciliationTaskIdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCK_ROLLOUTS_CREATE_RECONCILIATION_TASK_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsCreateReconciliationTaskIdErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_block_rollouts_create_reconciliation_task_id_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsCreateReconciliationTaskIdErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_RECONCILIATION_TASK_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_RECONCILIATION_TASK_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
