from typing import Literal

ApiV1KubernetesClustersRbacGrantsPartialUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsPartialUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_clusters_rbac_grants_partial_update_annotations_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsPartialUpdateAnnotationsErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
