from typing import Literal

ApiV1KubernetesClustersDiscoverCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersDiscoverCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_kubernetes_clusters_discover_create_criticality_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersDiscoverCreateCriticalityErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
