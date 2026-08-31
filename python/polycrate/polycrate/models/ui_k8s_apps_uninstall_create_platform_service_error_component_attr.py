from typing import Literal

UiK8SAppsUninstallCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

UI_K8S_APPS_UNINSTALL_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_ui_k8s_apps_uninstall_create_platform_service_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreatePlatformServiceErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
