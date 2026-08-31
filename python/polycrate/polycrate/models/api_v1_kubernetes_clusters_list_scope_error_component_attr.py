from typing import Literal

ApiV1KubernetesClustersListScopeErrorComponentAttr = Literal["scope"]

API_V1_KUBERNETES_CLUSTERS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersListScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_kubernetes_clusters_list_scope_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersListScopeErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
