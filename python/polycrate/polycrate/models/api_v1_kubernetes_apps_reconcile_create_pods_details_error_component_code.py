from typing import Literal

ApiV1KubernetesAppsReconcileCreatePodsDetailsErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_PODS_DETAILS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsReconcileCreatePodsDetailsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_reconcile_create_pods_details_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreatePodsDetailsErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_PODS_DETAILS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_PODS_DETAILS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
