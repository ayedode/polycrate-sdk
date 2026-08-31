from typing import Literal

ApiV1GrafanaDashboardSubscriptionsPartialUpdateDashboardErrorComponentAttr = Literal["dashboard"]

API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_PARTIAL_UPDATE_DASHBOARD_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1GrafanaDashboardSubscriptionsPartialUpdateDashboardErrorComponentAttr
] = {
    "dashboard",
}


def check_api_v1_grafana_dashboard_subscriptions_partial_update_dashboard_error_component_attr(
    value: str,
) -> ApiV1GrafanaDashboardSubscriptionsPartialUpdateDashboardErrorComponentAttr:
    if value in API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_PARTIAL_UPDATE_DASHBOARD_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_PARTIAL_UPDATE_DASHBOARD_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
