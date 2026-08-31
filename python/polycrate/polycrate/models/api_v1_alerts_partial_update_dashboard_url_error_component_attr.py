from typing import Literal

ApiV1AlertsPartialUpdateDashboardUrlErrorComponentAttr = Literal["dashboard_url"]

API_V1_ALERTS_PARTIAL_UPDATE_DASHBOARD_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsPartialUpdateDashboardUrlErrorComponentAttr
] = {
    "dashboard_url",
}


def check_api_v1_alerts_partial_update_dashboard_url_error_component_attr(
    value: str,
) -> ApiV1AlertsPartialUpdateDashboardUrlErrorComponentAttr:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_DASHBOARD_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_DASHBOARD_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
