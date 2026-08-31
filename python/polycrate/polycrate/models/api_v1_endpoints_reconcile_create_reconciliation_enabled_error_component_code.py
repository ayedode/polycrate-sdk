from typing import Literal

ApiV1EndpointsReconcileCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_ENDPOINTS_RECONCILE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsReconcileCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_endpoints_reconcile_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1EndpointsReconcileCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
