from typing import Literal

ApiV1KubernetesClustersReconcileCreateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersReconcileCreateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_clusters_reconcile_create_scope_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersReconcileCreateScopeErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
