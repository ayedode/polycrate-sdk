from typing import Literal

ApiV1AlertsReconcileCreateSuppressedErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTS_RECONCILE_CREATE_SUPPRESSED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsReconcileCreateSuppressedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alerts_reconcile_create_suppressed_error_component_code(
    value: str,
) -> ApiV1AlertsReconcileCreateSuppressedErrorComponentCode:
    if value in API_V1_ALERTS_RECONCILE_CREATE_SUPPRESSED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_SUPPRESSED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
