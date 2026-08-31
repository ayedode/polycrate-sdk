from typing import Literal

UiK8SAppsUninstallCreateLastInstallationErrorComponentAttr = Literal["last_installation"]

UI_K8S_APPS_UNINSTALL_CREATE_LAST_INSTALLATION_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateLastInstallationErrorComponentAttr
] = {
    "last_installation",
}


def check_ui_k8s_apps_uninstall_create_last_installation_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateLastInstallationErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_LAST_INSTALLATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_LAST_INSTALLATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
