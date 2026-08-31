from typing import Literal

ApiV1KubernetesAddonConfigRevisionsCreateBlockConfigTemplateErrorComponentAttr = Literal["block_config_template"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsCreateBlockConfigTemplateErrorComponentAttr
] = {
    "block_config_template",
}


def check_api_v1_kubernetes_addon_config_revisions_create_block_config_template_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsCreateBlockConfigTemplateErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
