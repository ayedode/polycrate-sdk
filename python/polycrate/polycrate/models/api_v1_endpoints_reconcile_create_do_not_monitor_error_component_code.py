from typing import Literal

ApiV1EndpointsReconcileCreateDoNotMonitorErrorComponentCode = Literal["invalid", "null"]

API_V1_ENDPOINTS_RECONCILE_CREATE_DO_NOT_MONITOR_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsReconcileCreateDoNotMonitorErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_endpoints_reconcile_create_do_not_monitor_error_component_code(
    value: str,
) -> ApiV1EndpointsReconcileCreateDoNotMonitorErrorComponentCode:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_DO_NOT_MONITOR_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_DO_NOT_MONITOR_ERROR_COMPONENT_CODE_VALUES!r}"
    )
