from typing import Literal

UiK8SAppsInstallCreateProviderErrorComponentAttr = Literal["provider"]

UI_K8S_APPS_INSTALL_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_ui_k8s_apps_install_create_provider_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateProviderErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
