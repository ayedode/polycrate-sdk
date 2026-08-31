from typing import Literal

ApiV1KubernetesAppsReconcileCreatePodsStatusUpdatedAtErrorComponentAttr = Literal["pods_status_updated_at"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_PODS_STATUS_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsReconcileCreatePodsStatusUpdatedAtErrorComponentAttr
] = {
    "pods_status_updated_at",
}


def check_api_v1_kubernetes_apps_reconcile_create_pods_status_updated_at_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreatePodsStatusUpdatedAtErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_PODS_STATUS_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_PODS_STATUS_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
