from typing import Literal

ApiV1KubernetesClustersDiscoverCreateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersDiscoverCreateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_clusters_discover_create_scope_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersDiscoverCreateScopeErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
