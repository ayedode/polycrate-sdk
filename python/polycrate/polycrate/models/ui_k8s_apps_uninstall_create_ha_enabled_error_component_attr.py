from typing import Literal

UiK8SAppsUninstallCreateHaEnabledErrorComponentAttr = Literal["ha_enabled"]

UI_K8S_APPS_UNINSTALL_CREATE_HA_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateHaEnabledErrorComponentAttr
] = {
    "ha_enabled",
}


def check_ui_k8s_apps_uninstall_create_ha_enabled_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateHaEnabledErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_HA_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_HA_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
