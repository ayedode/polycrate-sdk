from typing import Literal

ApiV1OrganizationsListGrafanaDashboardErrorComponentAttr = Literal["grafana_dashboard"]

API_V1_ORGANIZATIONS_LIST_GRAFANA_DASHBOARD_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsListGrafanaDashboardErrorComponentAttr
] = {
    "grafana_dashboard",
}


def check_api_v1_organizations_list_grafana_dashboard_error_component_attr(
    value: str,
) -> ApiV1OrganizationsListGrafanaDashboardErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_LIST_GRAFANA_DASHBOARD_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_LIST_GRAFANA_DASHBOARD_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
