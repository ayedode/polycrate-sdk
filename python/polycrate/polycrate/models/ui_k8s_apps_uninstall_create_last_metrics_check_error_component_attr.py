from typing import Literal

UiK8SAppsUninstallCreateLastMetricsCheckErrorComponentAttr = Literal["last_metrics_check"]

UI_K8S_APPS_UNINSTALL_CREATE_LAST_METRICS_CHECK_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateLastMetricsCheckErrorComponentAttr
] = {
    "last_metrics_check",
}


def check_ui_k8s_apps_uninstall_create_last_metrics_check_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateLastMetricsCheckErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_LAST_METRICS_CHECK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_LAST_METRICS_CHECK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
