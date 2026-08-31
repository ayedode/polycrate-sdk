from typing import Literal

UiK8SAppsUninstallCreateProviderIdErrorComponentAttr = Literal["provider_id"]

UI_K8S_APPS_UNINSTALL_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_ui_k8s_apps_uninstall_create_provider_id_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateProviderIdErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
