from typing import Literal

UiK8SAppsInstallCreateKindErrorComponentAttr = Literal["kind"]

UI_K8S_APPS_INSTALL_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[UiK8SAppsInstallCreateKindErrorComponentAttr] = {
    "kind",
}


def check_ui_k8s_apps_install_create_kind_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateKindErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
