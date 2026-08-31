from typing import Literal

ApiV1KubernetesClustersUpdateIsHostClusterErrorComponentCode = Literal["invalid", "null", "unique"]

API_V1_KUBERNETES_CLUSTERS_UPDATE_IS_HOST_CLUSTER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersUpdateIsHostClusterErrorComponentCode
] = {
    "invalid",
    "null",
    "unique",
}


def check_api_v1_kubernetes_clusters_update_is_host_cluster_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersUpdateIsHostClusterErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_UPDATE_IS_HOST_CLUSTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_UPDATE_IS_HOST_CLUSTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
