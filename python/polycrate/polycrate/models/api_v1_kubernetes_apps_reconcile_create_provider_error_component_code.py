from typing import Literal

ApiV1KubernetesAppsReconcileCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_apps_reconcile_create_provider_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateProviderErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
