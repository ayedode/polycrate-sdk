from typing import Literal

ApiV1KubernetesClustersDiscoverCreateSlugErrorComponentAttr = Literal["slug"]

API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersDiscoverCreateSlugErrorComponentAttr
] = {
    "slug",
}


def check_api_v1_kubernetes_clusters_discover_create_slug_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersDiscoverCreateSlugErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
