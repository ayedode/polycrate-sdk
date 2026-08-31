from typing import Literal

ApiV1KubernetesAppsReconcileCreateLastMetricsCheckErrorComponentAttr = Literal["last_metrics_check"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_LAST_METRICS_CHECK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateLastMetricsCheckErrorComponentAttr
] = {
    "last_metrics_check",
}


def check_api_v1_kubernetes_apps_reconcile_create_last_metrics_check_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateLastMetricsCheckErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_LAST_METRICS_CHECK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_LAST_METRICS_CHECK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
