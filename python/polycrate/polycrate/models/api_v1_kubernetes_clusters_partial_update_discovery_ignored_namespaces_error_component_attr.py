from typing import Literal

ApiV1KubernetesClustersPartialUpdateDiscoveryIgnoredNamespacesErrorComponentAttr = Literal[
    "discovery_ignored_namespaces"
]

API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_DISCOVERY_IGNORED_NAMESPACES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersPartialUpdateDiscoveryIgnoredNamespacesErrorComponentAttr
] = {
    "discovery_ignored_namespaces",
}


def check_api_v1_kubernetes_clusters_partial_update_discovery_ignored_namespaces_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersPartialUpdateDiscoveryIgnoredNamespacesErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_DISCOVERY_IGNORED_NAMESPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_DISCOVERY_IGNORED_NAMESPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
