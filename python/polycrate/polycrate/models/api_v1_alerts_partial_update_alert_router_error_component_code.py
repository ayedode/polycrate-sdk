from typing import Literal

ApiV1AlertsPartialUpdateAlertRouterErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ALERTS_PARTIAL_UPDATE_ALERT_ROUTER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsPartialUpdateAlertRouterErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_alerts_partial_update_alert_router_error_component_code(
    value: str,
) -> ApiV1AlertsPartialUpdateAlertRouterErrorComponentCode:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_ALERT_ROUTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_ALERT_ROUTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
