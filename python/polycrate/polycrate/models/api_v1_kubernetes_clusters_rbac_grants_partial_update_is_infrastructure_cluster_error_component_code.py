from typing import Literal

ApiV1KubernetesClustersRbacGrantsPartialUpdateIsInfrastructureClusterErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_IS_INFRASTRUCTURE_CLUSTER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsPartialUpdateIsInfrastructureClusterErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_clusters_rbac_grants_partial_update_is_infrastructure_cluster_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsPartialUpdateIsInfrastructureClusterErrorComponentCode:
    if (
        value
        in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_IS_INFRASTRUCTURE_CLUSTER_ERROR_COMPONENT_CODE_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_IS_INFRASTRUCTURE_CLUSTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
