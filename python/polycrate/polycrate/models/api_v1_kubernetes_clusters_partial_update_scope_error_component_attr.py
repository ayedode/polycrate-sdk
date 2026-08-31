from typing import Literal

ApiV1KubernetesClustersPartialUpdateScopeErrorComponentAttr = Literal["scope"]

API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersPartialUpdateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_kubernetes_clusters_partial_update_scope_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersPartialUpdateScopeErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
