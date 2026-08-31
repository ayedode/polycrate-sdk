from typing import Literal

ApiV1KubernetesAppsCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_KUBERNETES_APPS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_kubernetes_apps_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsCreateDebugModeErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
