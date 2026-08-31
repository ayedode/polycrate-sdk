from typing import Literal

ApiV1KubernetesAppsUpdateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsUpdateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_update_debug_mode_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsUpdateDebugModeErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
