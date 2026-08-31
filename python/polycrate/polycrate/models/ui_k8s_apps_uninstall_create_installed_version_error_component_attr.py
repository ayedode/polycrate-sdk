from typing import Literal

UiK8SAppsUninstallCreateInstalledVersionErrorComponentAttr = Literal["installed_version"]

UI_K8S_APPS_UNINSTALL_CREATE_INSTALLED_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateInstalledVersionErrorComponentAttr
] = {
    "installed_version",
}


def check_ui_k8s_apps_uninstall_create_installed_version_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateInstalledVersionErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_INSTALLED_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_INSTALLED_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
