from typing import Literal

UiK8SAppsUninstallCreateUninstalledErrorComponentCode = Literal["invalid", "null"]

UI_K8S_APPS_UNINSTALL_CREATE_UNINSTALLED_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsUninstallCreateUninstalledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_ui_k8s_apps_uninstall_create_uninstalled_error_component_code(
    value: str,
) -> UiK8SAppsUninstallCreateUninstalledErrorComponentCode:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_UNINSTALLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_UNINSTALLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
