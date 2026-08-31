from typing import Literal

UiK8SAppsUninstallCreateUninstallationRunningErrorComponentCode = Literal["invalid", "null"]

UI_K8S_APPS_UNINSTALL_CREATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsUninstallCreateUninstallationRunningErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_ui_k8s_apps_uninstall_create_uninstallation_running_error_component_code(
    value: str,
) -> UiK8SAppsUninstallCreateUninstallationRunningErrorComponentCode:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_CODE_VALUES!r}"
    )
