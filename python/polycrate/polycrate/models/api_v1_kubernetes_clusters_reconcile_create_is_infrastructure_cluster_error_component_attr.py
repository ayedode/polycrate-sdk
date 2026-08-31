from typing import Literal

ApiV1KubernetesClustersReconcileCreateIsInfrastructureClusterErrorComponentAttr = Literal["is_infrastructure_cluster"]

API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_IS_INFRASTRUCTURE_CLUSTER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersReconcileCreateIsInfrastructureClusterErrorComponentAttr
] = {
    "is_infrastructure_cluster",
}


def check_api_v1_kubernetes_clusters_reconcile_create_is_infrastructure_cluster_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersReconcileCreateIsInfrastructureClusterErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_IS_INFRASTRUCTURE_CLUSTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_IS_INFRASTRUCTURE_CLUSTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
