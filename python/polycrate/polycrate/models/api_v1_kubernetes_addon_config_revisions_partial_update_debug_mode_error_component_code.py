from typing import Literal

ApiV1KubernetesAddonConfigRevisionsPartialUpdateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsPartialUpdateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_addon_config_revisions_partial_update_debug_mode_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsPartialUpdateDebugModeErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
