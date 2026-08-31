from typing import Literal

ApiV1GrafanaDashboardSubscriptionsPartialUpdateRevisionErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_PARTIAL_UPDATE_REVISION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1GrafanaDashboardSubscriptionsPartialUpdateRevisionErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_grafana_dashboard_subscriptions_partial_update_revision_error_component_code(
    value: str,
) -> ApiV1GrafanaDashboardSubscriptionsPartialUpdateRevisionErrorComponentCode:
    if value in API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_PARTIAL_UPDATE_REVISION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_PARTIAL_UPDATE_REVISION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
