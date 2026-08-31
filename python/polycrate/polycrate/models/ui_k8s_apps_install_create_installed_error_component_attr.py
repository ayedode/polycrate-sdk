from typing import Literal

UiK8SAppsInstallCreateInstalledErrorComponentAttr = Literal["installed"]

UI_K8S_APPS_INSTALL_CREATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateInstalledErrorComponentAttr
] = {
    "installed",
}


def check_ui_k8s_apps_install_create_installed_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateInstalledErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
