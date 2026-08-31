from typing import Literal

UiK8SAppsUninstallCreateSloWindowDaysErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

UI_K8S_APPS_UNINSTALL_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsUninstallCreateSloWindowDaysErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_ui_k8s_apps_uninstall_create_slo_window_days_error_component_code(
    value: str,
) -> UiK8SAppsUninstallCreateSloWindowDaysErrorComponentCode:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
