from typing import Literal

ApiV1KubernetesAddonsCreateTemplateBlockErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_ADDONS_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsCreateTemplateBlockErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_addons_create_template_block_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsCreateTemplateBlockErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
