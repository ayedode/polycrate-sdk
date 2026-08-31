from typing import Literal

UiK8SAppsUninstallCreatePodsAvailableErrorComponentAttr = Literal["pods_available"]

UI_K8S_APPS_UNINSTALL_CREATE_PODS_AVAILABLE_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreatePodsAvailableErrorComponentAttr
] = {
    "pods_available",
}


def check_ui_k8s_apps_uninstall_create_pods_available_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreatePodsAvailableErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_PODS_AVAILABLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_PODS_AVAILABLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
