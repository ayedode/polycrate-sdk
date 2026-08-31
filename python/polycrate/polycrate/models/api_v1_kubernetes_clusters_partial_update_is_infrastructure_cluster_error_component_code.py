from typing import Literal

ApiV1KubernetesClustersPartialUpdateIsInfrastructureClusterErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_IS_INFRASTRUCTURE_CLUSTER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersPartialUpdateIsInfrastructureClusterErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_clusters_partial_update_is_infrastructure_cluster_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersPartialUpdateIsInfrastructureClusterErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_IS_INFRASTRUCTURE_CLUSTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_IS_INFRASTRUCTURE_CLUSTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
