from typing import Literal

UiK8SAppsInstallCreateLastInstallationErrorComponentAttr = Literal["last_installation"]

UI_K8S_APPS_INSTALL_CREATE_LAST_INSTALLATION_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateLastInstallationErrorComponentAttr
] = {
    "last_installation",
}


def check_ui_k8s_apps_install_create_last_installation_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateLastInstallationErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_LAST_INSTALLATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_LAST_INSTALLATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
