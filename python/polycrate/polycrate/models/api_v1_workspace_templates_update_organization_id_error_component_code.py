from typing import Literal

ApiV1WorkspaceTemplatesUpdateOrganizationIdErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACE_TEMPLATES_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspaceTemplatesUpdateOrganizationIdErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspace_templates_update_organization_id_error_component_code(
    value: str,
) -> ApiV1WorkspaceTemplatesUpdateOrganizationIdErrorComponentCode:
    if value in API_V1_WORKSPACE_TEMPLATES_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
