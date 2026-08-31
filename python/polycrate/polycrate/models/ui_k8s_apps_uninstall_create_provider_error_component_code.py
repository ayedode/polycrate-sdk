from typing import Literal

UiK8SAppsUninstallCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

UI_K8S_APPS_UNINSTALL_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsUninstallCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_ui_k8s_apps_uninstall_create_provider_error_component_code(
    value: str,
) -> UiK8SAppsUninstallCreateProviderErrorComponentCode:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
