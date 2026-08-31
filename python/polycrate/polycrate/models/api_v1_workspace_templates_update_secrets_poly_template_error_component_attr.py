from typing import Literal

ApiV1WorkspaceTemplatesUpdateSecretsPolyTemplateErrorComponentAttr = Literal["secrets_poly_template"]

API_V1_WORKSPACE_TEMPLATES_UPDATE_SECRETS_POLY_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspaceTemplatesUpdateSecretsPolyTemplateErrorComponentAttr
] = {
    "secrets_poly_template",
}


def check_api_v1_workspace_templates_update_secrets_poly_template_error_component_attr(
    value: str,
) -> ApiV1WorkspaceTemplatesUpdateSecretsPolyTemplateErrorComponentAttr:
    if value in API_V1_WORKSPACE_TEMPLATES_UPDATE_SECRETS_POLY_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_UPDATE_SECRETS_POLY_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
