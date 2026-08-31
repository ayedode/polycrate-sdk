from typing import Literal

ApiV1KubernetesAppsInstallCreateUninstallationRunningErrorComponentAttr = Literal["uninstallation_running"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsInstallCreateUninstallationRunningErrorComponentAttr
] = {
    "uninstallation_running",
}


def check_api_v1_kubernetes_apps_install_create_uninstallation_running_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateUninstallationRunningErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
