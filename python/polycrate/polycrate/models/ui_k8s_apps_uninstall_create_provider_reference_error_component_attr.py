from typing import Literal

UiK8SAppsUninstallCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

UI_K8S_APPS_UNINSTALL_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_ui_k8s_apps_uninstall_create_provider_reference_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateProviderReferenceErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
