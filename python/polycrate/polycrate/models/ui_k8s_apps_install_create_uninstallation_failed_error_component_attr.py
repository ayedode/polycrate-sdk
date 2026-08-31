from typing import Literal

UiK8SAppsInstallCreateUninstallationFailedErrorComponentAttr = Literal["uninstallation_failed"]

UI_K8S_APPS_INSTALL_CREATE_UNINSTALLATION_FAILED_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateUninstallationFailedErrorComponentAttr
] = {
    "uninstallation_failed",
}


def check_ui_k8s_apps_install_create_uninstallation_failed_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateUninstallationFailedErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_UNINSTALLATION_FAILED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_UNINSTALLATION_FAILED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
