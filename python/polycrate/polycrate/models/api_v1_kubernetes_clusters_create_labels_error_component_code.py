from typing import Literal

ApiV1KubernetesClustersCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_CLUSTERS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_clusters_create_labels_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersCreateLabelsErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
