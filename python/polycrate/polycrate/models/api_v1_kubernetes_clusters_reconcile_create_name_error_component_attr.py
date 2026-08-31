from typing import Literal

ApiV1KubernetesClustersReconcileCreateNameErrorComponentAttr = Literal["name"]

API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersReconcileCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_kubernetes_clusters_reconcile_create_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersReconcileCreateNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
