from typing import Literal

ApiV1KubernetesAddonsPartialUpdateTemplateBlockErrorComponentAttr = Literal["template_block"]

API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsPartialUpdateTemplateBlockErrorComponentAttr
] = {
    "template_block",
}


def check_api_v1_kubernetes_addons_partial_update_template_block_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsPartialUpdateTemplateBlockErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
