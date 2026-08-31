from typing import Literal

ApiV1KubernetesClustersCreateIsHostClusterErrorComponentAttr = Literal["is_host_cluster"]

API_V1_KUBERNETES_CLUSTERS_CREATE_IS_HOST_CLUSTER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersCreateIsHostClusterErrorComponentAttr
] = {
    "is_host_cluster",
}


def check_api_v1_kubernetes_clusters_create_is_host_cluster_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersCreateIsHostClusterErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_CREATE_IS_HOST_CLUSTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_CREATE_IS_HOST_CLUSTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
