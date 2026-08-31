from typing import Literal

ApiV1GrafanaDashboardSubscriptionsCreateOrganizationErrorComponentAttr = Literal["organization"]

API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_CREATE_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1GrafanaDashboardSubscriptionsCreateOrganizationErrorComponentAttr
] = {
    "organization",
}


def check_api_v1_grafana_dashboard_subscriptions_create_organization_error_component_attr(
    value: str,
) -> ApiV1GrafanaDashboardSubscriptionsCreateOrganizationErrorComponentAttr:
    if value in API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_CREATE_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_CREATE_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
