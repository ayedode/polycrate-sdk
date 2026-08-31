from typing import Literal

UiK8SAppsInstallCreateNameErrorComponentAttr = Literal["name"]

UI_K8S_APPS_INSTALL_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[UiK8SAppsInstallCreateNameErrorComponentAttr] = {
    "name",
}


def check_ui_k8s_apps_install_create_name_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateNameErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
