from typing import Literal

ApiV1WorkspaceTemplatesCreateOrganizationIdErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACE_TEMPLATES_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspaceTemplatesCreateOrganizationIdErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspace_templates_create_organization_id_error_component_code(
    value: str,
) -> ApiV1WorkspaceTemplatesCreateOrganizationIdErrorComponentCode:
    if value in API_V1_WORKSPACE_TEMPLATES_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
