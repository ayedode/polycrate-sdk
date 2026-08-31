from typing import Literal

ApiV1KubernetesClustersArchiveCreateIsInfrastructureClusterErrorComponentAttr = Literal["is_infrastructure_cluster"]

API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_IS_INFRASTRUCTURE_CLUSTER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersArchiveCreateIsInfrastructureClusterErrorComponentAttr
] = {
    "is_infrastructure_cluster",
}


def check_api_v1_kubernetes_clusters_archive_create_is_infrastructure_cluster_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersArchiveCreateIsInfrastructureClusterErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_IS_INFRASTRUCTURE_CLUSTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_IS_INFRASTRUCTURE_CLUSTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
