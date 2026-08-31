from typing import Literal

ApiV1KubernetesClustersRbacGrantsCreateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsCreateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_clusters_rbac_grants_create_scope_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsCreateScopeErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
