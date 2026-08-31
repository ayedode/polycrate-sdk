from typing import Literal

ApiV1KubernetesClustersUpdateIsInfrastructureClusterErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_CLUSTERS_UPDATE_IS_INFRASTRUCTURE_CLUSTER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersUpdateIsInfrastructureClusterErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_clusters_update_is_infrastructure_cluster_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersUpdateIsInfrastructureClusterErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_UPDATE_IS_INFRASTRUCTURE_CLUSTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_UPDATE_IS_INFRASTRUCTURE_CLUSTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
