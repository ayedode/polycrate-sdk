from typing import Literal

ApiV1AlertsReconcileCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTS_RECONCILE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsReconcileCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alerts_reconcile_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1AlertsReconcileCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_ALERTS_RECONCILE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
