from typing import Literal

ApiV1AlertsCreateAlertRouterErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ALERTS_CREATE_ALERT_ROUTER_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsCreateAlertRouterErrorComponentCode] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_alerts_create_alert_router_error_component_code(
    value: str,
) -> ApiV1AlertsCreateAlertRouterErrorComponentCode:
    if value in API_V1_ALERTS_CREATE_ALERT_ROUTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_CREATE_ALERT_ROUTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
