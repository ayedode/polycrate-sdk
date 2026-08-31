from typing import Literal

UiK8SAppsInstallCreateSlaWindowDaysErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

UI_K8S_APPS_INSTALL_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsInstallCreateSlaWindowDaysErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_ui_k8s_apps_install_create_sla_window_days_error_component_code(
    value: str,
) -> UiK8SAppsInstallCreateSlaWindowDaysErrorComponentCode:
    if value in UI_K8S_APPS_INSTALL_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
