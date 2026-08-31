from typing import Literal

ApiV1KubernetesClustersDiscoverCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersDiscoverCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_clusters_discover_create_annotations_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersDiscoverCreateAnnotationsErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
