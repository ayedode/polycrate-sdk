from typing import Literal

ApiV1WorkspaceTemplatesCreateSecretsPolyTemplateErrorComponentAttr = Literal["secrets_poly_template"]

API_V1_WORKSPACE_TEMPLATES_CREATE_SECRETS_POLY_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspaceTemplatesCreateSecretsPolyTemplateErrorComponentAttr
] = {
    "secrets_poly_template",
}


def check_api_v1_workspace_templates_create_secrets_poly_template_error_component_attr(
    value: str,
) -> ApiV1WorkspaceTemplatesCreateSecretsPolyTemplateErrorComponentAttr:
    if value in API_V1_WORKSPACE_TEMPLATES_CREATE_SECRETS_POLY_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_CREATE_SECRETS_POLY_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
