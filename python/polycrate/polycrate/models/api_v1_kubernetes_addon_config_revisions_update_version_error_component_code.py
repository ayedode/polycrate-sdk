from typing import Literal

ApiV1KubernetesAddonConfigRevisionsUpdateVersionErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_VERSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsUpdateVersionErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_addon_config_revisions_update_version_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsUpdateVersionErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
