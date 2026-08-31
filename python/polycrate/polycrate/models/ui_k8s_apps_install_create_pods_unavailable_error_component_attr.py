from typing import Literal

UiK8SAppsInstallCreatePodsUnavailableErrorComponentAttr = Literal["pods_unavailable"]

UI_K8S_APPS_INSTALL_CREATE_PODS_UNAVAILABLE_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreatePodsUnavailableErrorComponentAttr
] = {
    "pods_unavailable",
}


def check_ui_k8s_apps_install_create_pods_unavailable_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreatePodsUnavailableErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_PODS_UNAVAILABLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_PODS_UNAVAILABLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
