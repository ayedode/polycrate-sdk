from typing import Literal

ApiV1KubernetesClustersRbacGrantsCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_kubernetes_clusters_rbac_grants_create_criticality_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsCreateCriticalityErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
