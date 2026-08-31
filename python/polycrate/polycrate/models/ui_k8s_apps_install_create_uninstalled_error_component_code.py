from typing import Literal

UiK8SAppsInstallCreateUninstalledErrorComponentCode = Literal["invalid", "null"]

UI_K8S_APPS_INSTALL_CREATE_UNINSTALLED_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsInstallCreateUninstalledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_ui_k8s_apps_install_create_uninstalled_error_component_code(
    value: str,
) -> UiK8SAppsInstallCreateUninstalledErrorComponentCode:
    if value in UI_K8S_APPS_INSTALL_CREATE_UNINSTALLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_UNINSTALLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
