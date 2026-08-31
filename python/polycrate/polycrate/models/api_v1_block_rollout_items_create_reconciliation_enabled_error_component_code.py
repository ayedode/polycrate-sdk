from typing import Literal

ApiV1BlockRolloutItemsCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollout_items_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
