from typing import Literal

UiK8SAppsUninstallCreateAnnotationsErrorComponentCode = Literal["invalid"]

UI_K8S_APPS_UNINSTALL_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsUninstallCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_ui_k8s_apps_uninstall_create_annotations_error_component_code(
    value: str,
) -> UiK8SAppsUninstallCreateAnnotationsErrorComponentCode:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
