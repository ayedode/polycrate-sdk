from typing import Literal

ApiV1KubernetesAppsReconcileCreateUninstallationFailedErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_UNINSTALLATION_FAILED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateUninstallationFailedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_reconcile_create_uninstallation_failed_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateUninstallationFailedErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_UNINSTALLATION_FAILED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_UNINSTALLATION_FAILED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
