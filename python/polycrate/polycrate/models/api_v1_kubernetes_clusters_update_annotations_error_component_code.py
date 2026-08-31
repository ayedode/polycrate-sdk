from typing import Literal

ApiV1KubernetesClustersUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_CLUSTERS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_clusters_update_annotations_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersUpdateAnnotationsErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
