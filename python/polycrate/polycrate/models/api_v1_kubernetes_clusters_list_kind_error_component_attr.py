from typing import Literal

ApiV1KubernetesClustersListKindErrorComponentAttr = Literal["kind"]

API_V1_KUBERNETES_CLUSTERS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersListKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_kubernetes_clusters_list_kind_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersListKindErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
