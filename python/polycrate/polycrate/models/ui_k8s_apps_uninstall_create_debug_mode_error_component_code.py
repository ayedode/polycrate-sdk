from typing import Literal

UiK8SAppsUninstallCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

UI_K8S_APPS_UNINSTALL_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsUninstallCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_ui_k8s_apps_uninstall_create_debug_mode_error_component_code(
    value: str,
) -> UiK8SAppsUninstallCreateDebugModeErrorComponentCode:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
