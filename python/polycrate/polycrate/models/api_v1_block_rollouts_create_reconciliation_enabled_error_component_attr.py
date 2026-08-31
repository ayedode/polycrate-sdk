from typing import Literal

ApiV1BlockRolloutsCreateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_BLOCK_ROLLOUTS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsCreateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_block_rollouts_create_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsCreateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
