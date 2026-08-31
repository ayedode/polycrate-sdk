from typing import Literal

UiK8SAppsUninstallCreateLabelsErrorComponentCode = Literal["invalid"]

UI_K8S_APPS_UNINSTALL_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsUninstallCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_ui_k8s_apps_uninstall_create_labels_error_component_code(
    value: str,
) -> UiK8SAppsUninstallCreateLabelsErrorComponentCode:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
