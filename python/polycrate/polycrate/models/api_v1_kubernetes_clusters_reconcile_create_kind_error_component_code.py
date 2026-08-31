from typing import Literal

ApiV1KubernetesClustersReconcileCreateKindErrorComponentCode = Literal["invalid_choice", "null", "required"]

API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersReconcileCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
    "required",
}


def check_api_v1_kubernetes_clusters_reconcile_create_kind_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersReconcileCreateKindErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
