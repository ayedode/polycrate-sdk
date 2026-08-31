from typing import Literal

ApiV1KubernetesAddonsArchiveCreateDefaultBlockConfigTemplateErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_DEFAULT_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsArchiveCreateDefaultBlockConfigTemplateErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_addons_archive_create_default_block_config_template_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsArchiveCreateDefaultBlockConfigTemplateErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_DEFAULT_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_DEFAULT_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
