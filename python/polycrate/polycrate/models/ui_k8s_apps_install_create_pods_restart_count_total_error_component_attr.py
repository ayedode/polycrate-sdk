from typing import Literal

UiK8SAppsInstallCreatePodsRestartCountTotalErrorComponentAttr = Literal["pods_restart_count_total"]

UI_K8S_APPS_INSTALL_CREATE_PODS_RESTART_COUNT_TOTAL_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreatePodsRestartCountTotalErrorComponentAttr
] = {
    "pods_restart_count_total",
}


def check_ui_k8s_apps_install_create_pods_restart_count_total_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreatePodsRestartCountTotalErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_PODS_RESTART_COUNT_TOTAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_PODS_RESTART_COUNT_TOTAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
