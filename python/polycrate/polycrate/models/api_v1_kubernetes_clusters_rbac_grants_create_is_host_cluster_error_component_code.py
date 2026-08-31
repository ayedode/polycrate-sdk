from typing import Literal

ApiV1KubernetesClustersRbacGrantsCreateIsHostClusterErrorComponentCode = Literal["invalid", "null", "unique"]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_IS_HOST_CLUSTER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsCreateIsHostClusterErrorComponentCode
] = {
    "invalid",
    "null",
    "unique",
}


def check_api_v1_kubernetes_clusters_rbac_grants_create_is_host_cluster_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsCreateIsHostClusterErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_IS_HOST_CLUSTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_IS_HOST_CLUSTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
