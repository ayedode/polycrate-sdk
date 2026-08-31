from typing import Literal

UiK8SAppsUninstallCreatePodsReadyErrorComponentAttr = Literal["pods_ready"]

UI_K8S_APPS_UNINSTALL_CREATE_PODS_READY_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreatePodsReadyErrorComponentAttr
] = {
    "pods_ready",
}


def check_ui_k8s_apps_uninstall_create_pods_ready_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreatePodsReadyErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_PODS_READY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_PODS_READY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
