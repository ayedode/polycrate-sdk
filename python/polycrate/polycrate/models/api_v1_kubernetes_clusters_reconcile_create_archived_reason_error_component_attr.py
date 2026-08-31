from typing import Literal

ApiV1KubernetesClustersReconcileCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersReconcileCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_kubernetes_clusters_reconcile_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersReconcileCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
