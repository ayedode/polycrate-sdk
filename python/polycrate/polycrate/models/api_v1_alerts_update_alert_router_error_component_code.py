from typing import Literal

ApiV1AlertsUpdateAlertRouterErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ALERTS_UPDATE_ALERT_ROUTER_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsUpdateAlertRouterErrorComponentCode] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_alerts_update_alert_router_error_component_code(
    value: str,
) -> ApiV1AlertsUpdateAlertRouterErrorComponentCode:
    if value in API_V1_ALERTS_UPDATE_ALERT_ROUTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_ALERT_ROUTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
