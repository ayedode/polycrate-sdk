from typing import Literal

UiK8SAppsInstallCreateInstallationRunningErrorComponentAttr = Literal["installation_running"]

UI_K8S_APPS_INSTALL_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateInstallationRunningErrorComponentAttr
] = {
    "installation_running",
}


def check_ui_k8s_apps_install_create_installation_running_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateInstallationRunningErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
