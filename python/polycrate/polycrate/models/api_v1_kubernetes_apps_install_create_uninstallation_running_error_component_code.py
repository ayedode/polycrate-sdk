from typing import Literal

ApiV1KubernetesAppsInstallCreateUninstallationRunningErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsInstallCreateUninstallationRunningErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_install_create_uninstallation_running_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateUninstallationRunningErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_CODE_VALUES!r}"
    )
