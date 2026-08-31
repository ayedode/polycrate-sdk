from typing import Literal

ApiV1KubernetesAppsReconcileCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsReconcileCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_reconcile_create_platform_service_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreatePlatformServiceErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
