from typing import Literal

UiK8SAppsInstallCreatePodsRestartCountTotalErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

UI_K8S_APPS_INSTALL_CREATE_PODS_RESTART_COUNT_TOTAL_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsInstallCreatePodsRestartCountTotalErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_ui_k8s_apps_install_create_pods_restart_count_total_error_component_code(
    value: str,
) -> UiK8SAppsInstallCreatePodsRestartCountTotalErrorComponentCode:
    if value in UI_K8S_APPS_INSTALL_CREATE_PODS_RESTART_COUNT_TOTAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_PODS_RESTART_COUNT_TOTAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
