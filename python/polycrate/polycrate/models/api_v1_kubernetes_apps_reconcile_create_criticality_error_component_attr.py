from typing import Literal

ApiV1KubernetesAppsReconcileCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_kubernetes_apps_reconcile_create_criticality_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateCriticalityErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
