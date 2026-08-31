from typing import Literal

UiK8SAppsInstallCreateByoaErrorComponentAttr = Literal["byoa"]

UI_K8S_APPS_INSTALL_CREATE_BYOA_ERROR_COMPONENT_ATTR_VALUES: set[UiK8SAppsInstallCreateByoaErrorComponentAttr] = {
    "byoa",
}


def check_ui_k8s_apps_install_create_byoa_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateByoaErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_BYOA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_BYOA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
