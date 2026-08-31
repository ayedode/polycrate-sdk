from typing import Literal

UiK8SAppsInstallCreatePodsStatusUpdatedAtErrorComponentAttr = Literal["pods_status_updated_at"]

UI_K8S_APPS_INSTALL_CREATE_PODS_STATUS_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreatePodsStatusUpdatedAtErrorComponentAttr
] = {
    "pods_status_updated_at",
}


def check_ui_k8s_apps_install_create_pods_status_updated_at_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreatePodsStatusUpdatedAtErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_PODS_STATUS_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_PODS_STATUS_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
