from typing import Literal

ApiV1KubernetesClustersDiscoverCreateKindErrorComponentAttr = Literal["kind"]

API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersDiscoverCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_kubernetes_clusters_discover_create_kind_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersDiscoverCreateKindErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
