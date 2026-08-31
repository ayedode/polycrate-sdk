from typing import Literal

ApiV1KubernetesAddonConfigRevisionsPartialUpdateBlockConfigTemplateErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_PARTIAL_UPDATE_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsPartialUpdateBlockConfigTemplateErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_addon_config_revisions_partial_update_block_config_template_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsPartialUpdateBlockConfigTemplateErrorComponentCode:
    if (
        value
        in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_PARTIAL_UPDATE_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_CODE_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_PARTIAL_UPDATE_BLOCK_CONFIG_TEMPLATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
