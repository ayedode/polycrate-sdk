from typing import Literal

ApiV1OrganizationsCreateGrafanaOrgIdErrorComponentAttr = Literal["grafana_org_id"]

API_V1_ORGANIZATIONS_CREATE_GRAFANA_ORG_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsCreateGrafanaOrgIdErrorComponentAttr
] = {
    "grafana_org_id",
}


def check_api_v1_organizations_create_grafana_org_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateGrafanaOrgIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_GRAFANA_ORG_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_GRAFANA_ORG_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
