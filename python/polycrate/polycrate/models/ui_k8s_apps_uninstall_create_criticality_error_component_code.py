from typing import Literal

UiK8SAppsUninstallCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

UI_K8S_APPS_UNINSTALL_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsUninstallCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_ui_k8s_apps_uninstall_create_criticality_error_component_code(
    value: str,
) -> UiK8SAppsUninstallCreateCriticalityErrorComponentCode:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
