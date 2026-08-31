from typing import Literal

UiK8SAppsInstallCreateInstallationFailedErrorComponentAttr = Literal["installation_failed"]

UI_K8S_APPS_INSTALL_CREATE_INSTALLATION_FAILED_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateInstallationFailedErrorComponentAttr
] = {
    "installation_failed",
}


def check_ui_k8s_apps_install_create_installation_failed_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateInstallationFailedErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_INSTALLATION_FAILED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_INSTALLATION_FAILED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
