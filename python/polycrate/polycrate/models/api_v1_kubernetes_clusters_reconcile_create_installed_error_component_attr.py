from typing import Literal

ApiV1KubernetesClustersReconcileCreateInstalledErrorComponentAttr = Literal["installed"]

API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersReconcileCreateInstalledErrorComponentAttr
] = {
    "installed",
}


def check_api_v1_kubernetes_clusters_reconcile_create_installed_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersReconcileCreateInstalledErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
