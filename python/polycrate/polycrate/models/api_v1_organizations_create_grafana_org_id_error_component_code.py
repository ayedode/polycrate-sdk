from typing import Literal

ApiV1OrganizationsCreateGrafanaOrgIdErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ORGANIZATIONS_CREATE_GRAFANA_ORG_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsCreateGrafanaOrgIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_organizations_create_grafana_org_id_error_component_code(
    value: str,
) -> ApiV1OrganizationsCreateGrafanaOrgIdErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_CREATE_GRAFANA_ORG_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_GRAFANA_ORG_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
