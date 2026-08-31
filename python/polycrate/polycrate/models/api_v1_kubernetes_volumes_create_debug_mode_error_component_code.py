from typing import Literal

ApiV1KubernetesVolumesCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_VOLUMES_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_volumes_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesCreateDebugModeErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
