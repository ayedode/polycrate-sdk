from typing import Literal

ApiV1KubernetesClustersReconcileCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersReconcileCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_kubernetes_clusters_reconcile_create_display_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersReconcileCreateDisplayNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
