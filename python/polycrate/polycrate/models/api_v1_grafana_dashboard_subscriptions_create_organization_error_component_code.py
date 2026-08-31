from typing import Literal

ApiV1GrafanaDashboardSubscriptionsCreateOrganizationErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "null", "required"
]

API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_CREATE_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1GrafanaDashboardSubscriptionsCreateOrganizationErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_grafana_dashboard_subscriptions_create_organization_error_component_code(
    value: str,
) -> ApiV1GrafanaDashboardSubscriptionsCreateOrganizationErrorComponentCode:
    if value in API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_CREATE_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_GRAFANA_DASHBOARD_SUBSCRIPTIONS_CREATE_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
