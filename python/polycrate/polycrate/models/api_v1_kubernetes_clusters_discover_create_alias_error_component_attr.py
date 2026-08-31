from typing import Literal

ApiV1KubernetesClustersDiscoverCreateAliasErrorComponentAttr = Literal["alias"]

API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersDiscoverCreateAliasErrorComponentAttr
] = {
    "alias",
}


def check_api_v1_kubernetes_clusters_discover_create_alias_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersDiscoverCreateAliasErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
