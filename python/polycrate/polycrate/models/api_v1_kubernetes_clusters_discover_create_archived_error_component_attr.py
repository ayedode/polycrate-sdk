from typing import Literal

ApiV1KubernetesClustersDiscoverCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersDiscoverCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_kubernetes_clusters_discover_create_archived_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersDiscoverCreateArchivedErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
