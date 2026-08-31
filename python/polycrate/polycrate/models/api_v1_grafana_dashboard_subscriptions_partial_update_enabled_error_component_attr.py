from typing import Literal

ApiV1GrafanaDashboardSubscriptionsPartialUpdateEnabledErrorComponentAttr = Literal["enabled"]

API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_PARTIAL_UPDATE_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1GrafanaDashboardSubscriptionsPartialUpdateEnabledErrorComponentAttr
] = {
    "enabled",
}


def check_api_v1_grafana_dashboard_subscriptions_partial_update_enabled_error_component_attr(
    value: str,
) -> ApiV1GrafanaDashboardSubscriptionsPartialUpdateEnabledErrorComponentAttr:
    if value in API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_PARTIAL_UPDATE_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_PARTIAL_UPDATE_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
