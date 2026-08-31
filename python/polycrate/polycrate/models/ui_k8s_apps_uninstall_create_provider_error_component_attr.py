from typing import Literal

UiK8SAppsUninstallCreateProviderErrorComponentAttr = Literal["provider"]

UI_K8S_APPS_UNINSTALL_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_ui_k8s_apps_uninstall_create_provider_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateProviderErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
