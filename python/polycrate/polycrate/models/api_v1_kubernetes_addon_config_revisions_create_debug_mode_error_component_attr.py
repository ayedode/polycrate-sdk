from typing import Literal

ApiV1KubernetesAddonConfigRevisionsCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_kubernetes_addon_config_revisions_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsCreateDebugModeErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
