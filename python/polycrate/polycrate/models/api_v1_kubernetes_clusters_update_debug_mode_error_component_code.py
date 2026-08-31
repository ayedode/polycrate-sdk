from typing import Literal

ApiV1KubernetesClustersUpdateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_CLUSTERS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersUpdateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_clusters_update_debug_mode_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersUpdateDebugModeErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
