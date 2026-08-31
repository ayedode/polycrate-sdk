from typing import Literal

ApiV1KubernetesAppsUpdateUninstallationRunningErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_UPDATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsUpdateUninstallationRunningErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_update_uninstallation_running_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsUpdateUninstallationRunningErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_UPDATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_CODE_VALUES!r}"
    )
