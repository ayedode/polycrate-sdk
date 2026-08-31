from typing import Literal

ApiV1KubernetesAppsReconcileCreateInstallationRunningErrorComponentAttr = Literal["installation_running"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateInstallationRunningErrorComponentAttr
] = {
    "installation_running",
}


def check_api_v1_kubernetes_apps_reconcile_create_installation_running_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateInstallationRunningErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
