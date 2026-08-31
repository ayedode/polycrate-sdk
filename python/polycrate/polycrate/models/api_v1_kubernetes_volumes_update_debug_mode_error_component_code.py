from typing import Literal

ApiV1KubernetesVolumesUpdateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_VOLUMES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesUpdateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_volumes_update_debug_mode_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesUpdateDebugModeErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
