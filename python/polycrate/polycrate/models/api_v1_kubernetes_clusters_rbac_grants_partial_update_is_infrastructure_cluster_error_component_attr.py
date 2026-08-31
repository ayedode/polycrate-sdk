from typing import Literal

ApiV1KubernetesClustersRbacGrantsPartialUpdateIsInfrastructureClusterErrorComponentAttr = Literal[
    "is_infrastructure_cluster"
]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_IS_INFRASTRUCTURE_CLUSTER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsPartialUpdateIsInfrastructureClusterErrorComponentAttr
] = {
    "is_infrastructure_cluster",
}


def check_api_v1_kubernetes_clusters_rbac_grants_partial_update_is_infrastructure_cluster_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsPartialUpdateIsInfrastructureClusterErrorComponentAttr:
    if (
        value
        in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_IS_INFRASTRUCTURE_CLUSTER_ERROR_COMPONENT_ATTR_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_IS_INFRASTRUCTURE_CLUSTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
