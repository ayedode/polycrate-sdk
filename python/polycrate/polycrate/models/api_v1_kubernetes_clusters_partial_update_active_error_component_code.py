from typing import Literal

ApiV1KubernetesClustersPartialUpdateActiveErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersPartialUpdateActiveErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_clusters_partial_update_active_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersPartialUpdateActiveErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
