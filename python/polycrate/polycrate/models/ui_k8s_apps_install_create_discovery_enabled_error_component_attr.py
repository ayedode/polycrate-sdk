from typing import Literal

UiK8SAppsInstallCreateDiscoveryEnabledErrorComponentAttr = Literal["discovery_enabled"]

UI_K8S_APPS_INSTALL_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateDiscoveryEnabledErrorComponentAttr
] = {
    "discovery_enabled",
}


def check_ui_k8s_apps_install_create_discovery_enabled_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateDiscoveryEnabledErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
