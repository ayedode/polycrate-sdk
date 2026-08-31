from typing import Literal

ApiV1GrafanaDashboardSubscriptionsPartialUpdateEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_PARTIAL_UPDATE_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1GrafanaDashboardSubscriptionsPartialUpdateEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_grafana_dashboard_subscriptions_partial_update_enabled_error_component_code(
    value: str,
) -> ApiV1GrafanaDashboardSubscriptionsPartialUpdateEnabledErrorComponentCode:
    if value in API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_PARTIAL_UPDATE_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_PARTIAL_UPDATE_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
