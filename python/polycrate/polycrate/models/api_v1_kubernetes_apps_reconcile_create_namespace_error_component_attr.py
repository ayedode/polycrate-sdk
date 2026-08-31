from typing import Literal

ApiV1KubernetesAppsReconcileCreateNamespaceErrorComponentAttr = Literal["namespace"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateNamespaceErrorComponentAttr
] = {
    "namespace",
}


def check_api_v1_kubernetes_apps_reconcile_create_namespace_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateNamespaceErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
