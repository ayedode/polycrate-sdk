from typing import Literal

ApiV1KubernetesClustersArchiveCreateDiscoveryIgnoredNamespacesErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_DISCOVERY_IGNORED_NAMESPACES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersArchiveCreateDiscoveryIgnoredNamespacesErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_clusters_archive_create_discovery_ignored_namespaces_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersArchiveCreateDiscoveryIgnoredNamespacesErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_DISCOVERY_IGNORED_NAMESPACES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_DISCOVERY_IGNORED_NAMESPACES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
