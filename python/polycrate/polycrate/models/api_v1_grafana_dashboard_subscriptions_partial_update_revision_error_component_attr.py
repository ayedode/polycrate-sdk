from typing import Literal

ApiV1GrafanaDashboardSubscriptionsPartialUpdateRevisionErrorComponentAttr = Literal["revision"]

API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_PARTIAL_UPDATE_REVISION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1GrafanaDashboardSubscriptionsPartialUpdateRevisionErrorComponentAttr
] = {
    "revision",
}


def check_api_v1_grafana_dashboard_subscriptions_partial_update_revision_error_component_attr(
    value: str,
) -> ApiV1GrafanaDashboardSubscriptionsPartialUpdateRevisionErrorComponentAttr:
    if value in API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_PARTIAL_UPDATE_REVISION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_PARTIAL_UPDATE_REVISION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
