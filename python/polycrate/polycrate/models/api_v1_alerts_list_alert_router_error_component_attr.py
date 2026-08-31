from typing import Literal

ApiV1AlertsListAlertRouterErrorComponentAttr = Literal["alert_router"]

API_V1_ALERTS_LIST_ALERT_ROUTER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsListAlertRouterErrorComponentAttr] = {
    "alert_router",
}


def check_api_v1_alerts_list_alert_router_error_component_attr(
    value: str,
) -> ApiV1AlertsListAlertRouterErrorComponentAttr:
    if value in API_V1_ALERTS_LIST_ALERT_ROUTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_LIST_ALERT_ROUTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
