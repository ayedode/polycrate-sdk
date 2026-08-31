from typing import Literal

UiK8SAppsUninstallCreateNamespaceErrorComponentAttr = Literal["namespace"]

UI_K8S_APPS_UNINSTALL_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateNamespaceErrorComponentAttr
] = {
    "namespace",
}


def check_ui_k8s_apps_uninstall_create_namespace_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateNamespaceErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
