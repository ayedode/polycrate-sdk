from typing import Literal

ApiV1KubernetesClustersPartialUpdateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersPartialUpdateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_kubernetes_clusters_partial_update_debug_mode_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersPartialUpdateDebugModeErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
