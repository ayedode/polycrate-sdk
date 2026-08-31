from typing import Literal

ApiV1OrganizationsChoicesListGrafanaDashboardErrorComponentAttr = Literal["grafana_dashboard"]

API_V1_ORGANIZATIONS_CHOICES_LIST_GRAFANA_DASHBOARD_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsChoicesListGrafanaDashboardErrorComponentAttr
] = {
    "grafana_dashboard",
}


def check_api_v1_organizations_choices_list_grafana_dashboard_error_component_attr(
    value: str,
) -> ApiV1OrganizationsChoicesListGrafanaDashboardErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CHOICES_LIST_GRAFANA_DASHBOARD_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CHOICES_LIST_GRAFANA_DASHBOARD_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
