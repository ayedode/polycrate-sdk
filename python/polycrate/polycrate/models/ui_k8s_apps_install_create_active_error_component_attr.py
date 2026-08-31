from typing import Literal

UiK8SAppsInstallCreateActiveErrorComponentAttr = Literal["active"]

UI_K8S_APPS_INSTALL_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[UiK8SAppsInstallCreateActiveErrorComponentAttr] = {
    "active",
}


def check_ui_k8s_apps_install_create_active_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateActiveErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
