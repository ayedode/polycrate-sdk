from typing import Literal

ApiV1KubernetesClustersUpdateDiscoveryIgnoredNamespacesErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_CLUSTERS_UPDATE_DISCOVERY_IGNORED_NAMESPACES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersUpdateDiscoveryIgnoredNamespacesErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_clusters_update_discovery_ignored_namespaces_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersUpdateDiscoveryIgnoredNamespacesErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_UPDATE_DISCOVERY_IGNORED_NAMESPACES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_UPDATE_DISCOVERY_IGNORED_NAMESPACES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
