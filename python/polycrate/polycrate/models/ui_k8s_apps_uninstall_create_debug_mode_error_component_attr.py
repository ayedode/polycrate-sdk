from typing import Literal

UiK8SAppsUninstallCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

UI_K8S_APPS_UNINSTALL_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_ui_k8s_apps_uninstall_create_debug_mode_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateDebugModeErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
