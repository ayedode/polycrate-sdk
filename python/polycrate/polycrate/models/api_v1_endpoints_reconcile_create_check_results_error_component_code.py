from typing import Literal

ApiV1EndpointsReconcileCreateCheckResultsErrorComponentCode = Literal["invalid"]

API_V1_ENDPOINTS_RECONCILE_CREATE_CHECK_RESULTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsReconcileCreateCheckResultsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_endpoints_reconcile_create_check_results_error_component_code(
    value: str,
) -> ApiV1EndpointsReconcileCreateCheckResultsErrorComponentCode:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_CHECK_RESULTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_CHECK_RESULTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
