from typing import Literal

UiK8SAppsUninstallCreatePodsTotalErrorComponentAttr = Literal["pods_total"]

UI_K8S_APPS_UNINSTALL_CREATE_PODS_TOTAL_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreatePodsTotalErrorComponentAttr
] = {
    "pods_total",
}


def check_ui_k8s_apps_uninstall_create_pods_total_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreatePodsTotalErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_PODS_TOTAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_PODS_TOTAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
