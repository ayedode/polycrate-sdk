from typing import Literal

ApiV1GrafanaDashboardSubscriptionsCreateDashboardErrorComponentAttr = Literal["dashboard"]

API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_CREATE_DASHBOARD_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1GrafanaDashboardSubscriptionsCreateDashboardErrorComponentAttr
] = {
    "dashboard",
}


def check_api_v1_grafana_dashboard_subscriptions_create_dashboard_error_component_attr(
    value: str,
) -> ApiV1GrafanaDashboardSubscriptionsCreateDashboardErrorComponentAttr:
    if value in API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_CREATE_DASHBOARD_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_CREATE_DASHBOARD_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
