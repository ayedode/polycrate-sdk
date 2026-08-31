from typing import Literal

ApiV1KubernetesClustersUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_KUBERNETES_CLUSTERS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_kubernetes_clusters_update_labels_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersUpdateLabelsErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
