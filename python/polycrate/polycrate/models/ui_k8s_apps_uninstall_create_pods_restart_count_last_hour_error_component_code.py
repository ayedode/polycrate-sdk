from typing import Literal

UiK8SAppsUninstallCreatePodsRestartCountLastHourErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

UI_K8S_APPS_UNINSTALL_CREATE_PODS_RESTART_COUNT_LAST_HOUR_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsUninstallCreatePodsRestartCountLastHourErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_ui_k8s_apps_uninstall_create_pods_restart_count_last_hour_error_component_code(
    value: str,
) -> UiK8SAppsUninstallCreatePodsRestartCountLastHourErrorComponentCode:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_PODS_RESTART_COUNT_LAST_HOUR_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_PODS_RESTART_COUNT_LAST_HOUR_ERROR_COMPONENT_CODE_VALUES!r}"
    )
