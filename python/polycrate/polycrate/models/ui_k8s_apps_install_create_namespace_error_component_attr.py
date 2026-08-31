from typing import Literal

UiK8SAppsInstallCreateNamespaceErrorComponentAttr = Literal["namespace"]

UI_K8S_APPS_INSTALL_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateNamespaceErrorComponentAttr
] = {
    "namespace",
}


def check_ui_k8s_apps_install_create_namespace_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateNamespaceErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
