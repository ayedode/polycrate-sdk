from typing import Literal

ApiV1KubernetesAppsReconcileCreateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_apps_reconcile_create_scope_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateScopeErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
