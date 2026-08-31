from typing import Literal

ApiV1ConditionInstancesCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_CONDITION_INSTANCES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_condition_instances_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
