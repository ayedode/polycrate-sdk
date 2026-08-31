from typing import Literal

UiK8SAppsUninstallCreateHaEnabledErrorComponentCode = Literal["invalid"]

UI_K8S_APPS_UNINSTALL_CREATE_HA_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsUninstallCreateHaEnabledErrorComponentCode
] = {
    "invalid",
}


def check_ui_k8s_apps_uninstall_create_ha_enabled_error_component_code(
    value: str,
) -> UiK8SAppsUninstallCreateHaEnabledErrorComponentCode:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_HA_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_HA_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
