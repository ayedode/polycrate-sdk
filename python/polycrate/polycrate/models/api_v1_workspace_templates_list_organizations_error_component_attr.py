from typing import Literal

ApiV1WorkspaceTemplatesListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_WORKSPACE_TEMPLATES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspaceTemplatesListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_workspace_templates_list_organizations_error_component_attr(
    value: str,
) -> ApiV1WorkspaceTemplatesListOrganizationsErrorComponentAttr:
    if value in API_V1_WORKSPACE_TEMPLATES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
