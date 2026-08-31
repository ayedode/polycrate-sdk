from typing import Literal

ApiV1AlertsUpdateDashboardUrlErrorComponentAttr = Literal["dashboard_url"]

API_V1_ALERTS_UPDATE_DASHBOARD_URL_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsUpdateDashboardUrlErrorComponentAttr] = {
    "dashboard_url",
}


def check_api_v1_alerts_update_dashboard_url_error_component_attr(
    value: str,
) -> ApiV1AlertsUpdateDashboardUrlErrorComponentAttr:
    if value in API_V1_ALERTS_UPDATE_DASHBOARD_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_DASHBOARD_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
