from typing import Literal

ApiV1KubernetesClustersArchiveCreateIsHostClusterErrorComponentCode = Literal["invalid", "null", "unique"]

API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_IS_HOST_CLUSTER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersArchiveCreateIsHostClusterErrorComponentCode
] = {
    "invalid",
    "null",
    "unique",
}


def check_api_v1_kubernetes_clusters_archive_create_is_host_cluster_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersArchiveCreateIsHostClusterErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_IS_HOST_CLUSTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_IS_HOST_CLUSTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
