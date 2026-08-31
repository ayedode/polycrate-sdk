from typing import Literal

ApiV1KubernetesAddonConfigRevisionsUpdateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsUpdateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_kubernetes_addon_config_revisions_update_debug_mode_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsUpdateDebugModeErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
