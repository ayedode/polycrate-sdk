from typing import Literal

ApiV1AlertsReconcileCreateAlertRouterErrorComponentAttr = Literal["alert_router"]

API_V1_ALERTS_RECONCILE_CREATE_ALERT_ROUTER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsReconcileCreateAlertRouterErrorComponentAttr
] = {
    "alert_router",
}


def check_api_v1_alerts_reconcile_create_alert_router_error_component_attr(
    value: str,
) -> ApiV1AlertsReconcileCreateAlertRouterErrorComponentAttr:
    if value in API_V1_ALERTS_RECONCILE_CREATE_ALERT_ROUTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_ALERT_ROUTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
