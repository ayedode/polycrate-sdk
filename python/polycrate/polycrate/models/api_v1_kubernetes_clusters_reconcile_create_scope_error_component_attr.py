from typing import Literal

ApiV1KubernetesClustersReconcileCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersReconcileCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_kubernetes_clusters_reconcile_create_scope_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersReconcileCreateScopeErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
