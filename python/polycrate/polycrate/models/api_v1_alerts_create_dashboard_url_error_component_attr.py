from typing import Literal

ApiV1AlertsCreateDashboardUrlErrorComponentAttr = Literal["dashboard_url"]

API_V1_ALERTS_CREATE_DASHBOARD_URL_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsCreateDashboardUrlErrorComponentAttr] = {
    "dashboard_url",
}


def check_api_v1_alerts_create_dashboard_url_error_component_attr(
    value: str,
) -> ApiV1AlertsCreateDashboardUrlErrorComponentAttr:
    if value in API_V1_ALERTS_CREATE_DASHBOARD_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_CREATE_DASHBOARD_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
