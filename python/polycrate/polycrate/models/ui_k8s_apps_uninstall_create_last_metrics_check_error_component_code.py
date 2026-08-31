from typing import Literal

UiK8SAppsUninstallCreateLastMetricsCheckErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

UI_K8S_APPS_UNINSTALL_CREATE_LAST_METRICS_CHECK_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsUninstallCreateLastMetricsCheckErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_ui_k8s_apps_uninstall_create_last_metrics_check_error_component_code(
    value: str,
) -> UiK8SAppsUninstallCreateLastMetricsCheckErrorComponentCode:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_LAST_METRICS_CHECK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_LAST_METRICS_CHECK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
