from typing import Literal

UiK8SAppsUninstallCreateLabelsErrorComponentAttr = Literal["labels"]

UI_K8S_APPS_UNINSTALL_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_ui_k8s_apps_uninstall_create_labels_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateLabelsErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
