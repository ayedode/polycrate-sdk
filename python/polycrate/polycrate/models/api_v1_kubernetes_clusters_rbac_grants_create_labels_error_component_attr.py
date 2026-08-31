from typing import Literal

ApiV1KubernetesClustersRbacGrantsCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_kubernetes_clusters_rbac_grants_create_labels_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsCreateLabelsErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
