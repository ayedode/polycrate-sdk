from typing import Literal

ApiV1EndpointsReconcileCreateCheckResultRetentionDaysErrorComponentAttr = Literal["check_result_retention_days"]

API_V1_ENDPOINTS_RECONCILE_CREATE_CHECK_RESULT_RETENTION_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsReconcileCreateCheckResultRetentionDaysErrorComponentAttr
] = {
    "check_result_retention_days",
}


def check_api_v1_endpoints_reconcile_create_check_result_retention_days_error_component_attr(
    value: str,
) -> ApiV1EndpointsReconcileCreateCheckResultRetentionDaysErrorComponentAttr:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_CHECK_RESULT_RETENTION_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_CHECK_RESULT_RETENTION_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
