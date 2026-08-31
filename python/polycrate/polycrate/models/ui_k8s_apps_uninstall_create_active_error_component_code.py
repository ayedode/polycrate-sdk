from typing import Literal

UiK8SAppsUninstallCreateActiveErrorComponentCode = Literal["invalid", "null"]

UI_K8S_APPS_UNINSTALL_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsUninstallCreateActiveErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_ui_k8s_apps_uninstall_create_active_error_component_code(
    value: str,
) -> UiK8SAppsUninstallCreateActiveErrorComponentCode:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
