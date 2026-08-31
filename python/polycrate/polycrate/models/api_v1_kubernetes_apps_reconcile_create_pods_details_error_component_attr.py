from typing import Literal

ApiV1KubernetesAppsReconcileCreatePodsDetailsErrorComponentAttr = Literal["pods_details"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_PODS_DETAILS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsReconcileCreatePodsDetailsErrorComponentAttr
] = {
    "pods_details",
}


def check_api_v1_kubernetes_apps_reconcile_create_pods_details_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreatePodsDetailsErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_PODS_DETAILS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_PODS_DETAILS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
