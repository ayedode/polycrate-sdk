from typing import Literal

UiK8SAppsUninstallCreateAnnotationsErrorComponentAttr = Literal["annotations"]

UI_K8S_APPS_UNINSTALL_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_ui_k8s_apps_uninstall_create_annotations_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateAnnotationsErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
