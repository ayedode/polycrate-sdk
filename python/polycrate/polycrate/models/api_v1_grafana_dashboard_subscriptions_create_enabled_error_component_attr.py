from typing import Literal

ApiV1GrafanaDashboardSubscriptionsCreateEnabledErrorComponentAttr = Literal["enabled"]

API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_CREATE_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1GrafanaDashboardSubscriptionsCreateEnabledErrorComponentAttr
] = {
    "enabled",
}


def check_api_v1_grafana_dashboard_subscriptions_create_enabled_error_component_attr(
    value: str,
) -> ApiV1GrafanaDashboardSubscriptionsCreateEnabledErrorComponentAttr:
    if value in API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_CREATE_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_CREATE_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
