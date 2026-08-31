from typing import Literal

UiK8SAppsInstallCreatePodsReadyErrorComponentAttr = Literal["pods_ready"]

UI_K8S_APPS_INSTALL_CREATE_PODS_READY_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreatePodsReadyErrorComponentAttr
] = {
    "pods_ready",
}


def check_ui_k8s_apps_install_create_pods_ready_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreatePodsReadyErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_PODS_READY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_PODS_READY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
