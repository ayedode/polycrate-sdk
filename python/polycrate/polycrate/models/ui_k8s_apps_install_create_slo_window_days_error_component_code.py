from typing import Literal

UiK8SAppsInstallCreateSloWindowDaysErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

UI_K8S_APPS_INSTALL_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsInstallCreateSloWindowDaysErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_ui_k8s_apps_install_create_slo_window_days_error_component_code(
    value: str,
) -> UiK8SAppsInstallCreateSloWindowDaysErrorComponentCode:
    if value in UI_K8S_APPS_INSTALL_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
