from typing import Literal

UiK8SAppsInstallCreatePodsRestartCountLastHourErrorComponentAttr = Literal["pods_restart_count_last_hour"]

UI_K8S_APPS_INSTALL_CREATE_PODS_RESTART_COUNT_LAST_HOUR_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreatePodsRestartCountLastHourErrorComponentAttr
] = {
    "pods_restart_count_last_hour",
}


def check_ui_k8s_apps_install_create_pods_restart_count_last_hour_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreatePodsRestartCountLastHourErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_PODS_RESTART_COUNT_LAST_HOUR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_PODS_RESTART_COUNT_LAST_HOUR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
