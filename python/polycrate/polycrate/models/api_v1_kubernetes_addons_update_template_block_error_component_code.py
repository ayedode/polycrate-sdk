from typing import Literal

ApiV1KubernetesAddonsUpdateTemplateBlockErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_ADDONS_UPDATE_TEMPLATE_BLOCK_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsUpdateTemplateBlockErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_addons_update_template_block_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsUpdateTemplateBlockErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_UPDATE_TEMPLATE_BLOCK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_UPDATE_TEMPLATE_BLOCK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
