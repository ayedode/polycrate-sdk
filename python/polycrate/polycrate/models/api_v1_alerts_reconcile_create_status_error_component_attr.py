from typing import Literal

ApiV1AlertsReconcileCreateStatusErrorComponentAttr = Literal["status"]

API_V1_ALERTS_RECONCILE_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsReconcileCreateStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_alerts_reconcile_create_status_error_component_attr(
    value: str,
) -> ApiV1AlertsReconcileCreateStatusErrorComponentAttr:
    if value in API_V1_ALERTS_RECONCILE_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
