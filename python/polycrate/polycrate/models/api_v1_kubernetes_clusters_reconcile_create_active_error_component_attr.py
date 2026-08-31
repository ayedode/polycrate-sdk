from typing import Literal

ApiV1KubernetesClustersReconcileCreateActiveErrorComponentAttr = Literal["active"]

API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersReconcileCreateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_kubernetes_clusters_reconcile_create_active_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersReconcileCreateActiveErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
