from typing import Literal

UiK8SAppsInstallCreateInstallationRunningErrorComponentCode = Literal["invalid", "null"]

UI_K8S_APPS_INSTALL_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsInstallCreateInstallationRunningErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_ui_k8s_apps_install_create_installation_running_error_component_code(
    value: str,
) -> UiK8SAppsInstallCreateInstallationRunningErrorComponentCode:
    if value in UI_K8S_APPS_INSTALL_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_CODE_VALUES!r}"
    )
