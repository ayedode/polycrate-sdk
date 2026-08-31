from typing import Literal

ApiV1KubernetesClustersDiscoverCreateDiscoveryIgnoredNamespacesErrorComponentAttr = Literal[
    "discovery_ignored_namespaces"
]

API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_DISCOVERY_IGNORED_NAMESPACES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersDiscoverCreateDiscoveryIgnoredNamespacesErrorComponentAttr
] = {
    "discovery_ignored_namespaces",
}


def check_api_v1_kubernetes_clusters_discover_create_discovery_ignored_namespaces_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersDiscoverCreateDiscoveryIgnoredNamespacesErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_DISCOVERY_IGNORED_NAMESPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_DISCOVERY_IGNORED_NAMESPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
