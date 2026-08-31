from typing import Literal

UiK8SAppsUninstallCreatePodsDetailsErrorComponentAttr = Literal["pods_details"]

UI_K8S_APPS_UNINSTALL_CREATE_PODS_DETAILS_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreatePodsDetailsErrorComponentAttr
] = {
    "pods_details",
}


def check_ui_k8s_apps_uninstall_create_pods_details_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreatePodsDetailsErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_PODS_DETAILS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_PODS_DETAILS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
