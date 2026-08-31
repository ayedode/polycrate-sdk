from typing import Literal

ApiV1WorkspaceTemplatesUpdateOrganizationIdErrorComponentAttr = Literal["organization_id"]

API_V1_WORKSPACE_TEMPLATES_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspaceTemplatesUpdateOrganizationIdErrorComponentAttr
] = {
    "organization_id",
}


def check_api_v1_workspace_templates_update_organization_id_error_component_attr(
    value: str,
) -> ApiV1WorkspaceTemplatesUpdateOrganizationIdErrorComponentAttr:
    if value in API_V1_WORKSPACE_TEMPLATES_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
