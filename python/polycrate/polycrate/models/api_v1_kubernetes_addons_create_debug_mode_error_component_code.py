from typing import Literal

ApiV1KubernetesAddonsCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_ADDONS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_addons_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsCreateDebugModeErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
