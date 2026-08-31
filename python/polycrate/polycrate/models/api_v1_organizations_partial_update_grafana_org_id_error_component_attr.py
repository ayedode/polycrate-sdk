from typing import Literal

ApiV1OrganizationsPartialUpdateGrafanaOrgIdErrorComponentAttr = Literal["grafana_org_id"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_GRAFANA_ORG_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateGrafanaOrgIdErrorComponentAttr
] = {
    "grafana_org_id",
}


def check_api_v1_organizations_partial_update_grafana_org_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateGrafanaOrgIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_GRAFANA_ORG_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_GRAFANA_ORG_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
