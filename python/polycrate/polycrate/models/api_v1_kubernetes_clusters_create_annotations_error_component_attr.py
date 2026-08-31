from typing import Literal

ApiV1KubernetesClustersCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_KUBERNETES_CLUSTERS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_kubernetes_clusters_create_annotations_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersCreateAnnotationsErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
