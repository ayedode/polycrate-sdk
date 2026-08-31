from typing import Literal

ApiV1KubernetesClustersReconcileCreateManagedByObjectIdErrorComponentAttr = Literal["managed_by_object_id"]

API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersReconcileCreateManagedByObjectIdErrorComponentAttr
] = {
    "managed_by_object_id",
}


def check_api_v1_kubernetes_clusters_reconcile_create_managed_by_object_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersReconcileCreateManagedByObjectIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
