from typing import Literal

ApiV1KubernetesAddonsPartialUpdateDefaultBlockConfigTemplateErrorComponentAttr = Literal[
    "default_block_config_template"
]

API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_DEFAULT_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsPartialUpdateDefaultBlockConfigTemplateErrorComponentAttr
] = {
    "default_block_config_template",
}


def check_api_v1_kubernetes_addons_partial_update_default_block_config_template_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsPartialUpdateDefaultBlockConfigTemplateErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_DEFAULT_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_DEFAULT_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
