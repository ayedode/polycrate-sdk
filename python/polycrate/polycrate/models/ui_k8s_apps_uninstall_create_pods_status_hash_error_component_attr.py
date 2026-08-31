from typing import Literal

UiK8SAppsUninstallCreatePodsStatusHashErrorComponentAttr = Literal["pods_status_hash"]

UI_K8S_APPS_UNINSTALL_CREATE_PODS_STATUS_HASH_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreatePodsStatusHashErrorComponentAttr
] = {
    "pods_status_hash",
}


def check_ui_k8s_apps_uninstall_create_pods_status_hash_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreatePodsStatusHashErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_PODS_STATUS_HASH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_PODS_STATUS_HASH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
