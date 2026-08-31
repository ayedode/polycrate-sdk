from typing import Literal

UiK8SAppsInstallCreateBlockErrorComponentAttr = Literal["block"]

UI_K8S_APPS_INSTALL_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[UiK8SAppsInstallCreateBlockErrorComponentAttr] = {
    "block",
}


def check_ui_k8s_apps_install_create_block_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateBlockErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
