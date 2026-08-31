from typing import Literal

UiK8SAppsUninstallCreateUninstallationRunningErrorComponentAttr = Literal["uninstallation_running"]

UI_K8S_APPS_UNINSTALL_CREATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateUninstallationRunningErrorComponentAttr
] = {
    "uninstallation_running",
}


def check_ui_k8s_apps_uninstall_create_uninstallation_running_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateUninstallationRunningErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
