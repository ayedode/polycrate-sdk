from typing import Literal

ApiV1WorkspaceTemplatesListOrganizationsErrorComponentCode = Literal[
    "invalid_choice", "invalid_list", "invalid_pk_value"
]

API_V1_WORKSPACE_TEMPLATES_LIST_ORGANIZATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspaceTemplatesListOrganizationsErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_workspace_templates_list_organizations_error_component_code(
    value: str,
) -> ApiV1WorkspaceTemplatesListOrganizationsErrorComponentCode:
    if value in API_V1_WORKSPACE_TEMPLATES_LIST_ORGANIZATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_LIST_ORGANIZATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
