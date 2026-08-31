from typing import Literal

ApiV1KubernetesClustersReconcileCreateActiveErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersReconcileCreateActiveErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_clusters_reconcile_create_active_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersReconcileCreateActiveErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
