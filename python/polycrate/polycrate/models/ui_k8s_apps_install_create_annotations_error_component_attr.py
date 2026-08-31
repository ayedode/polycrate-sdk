from typing import Literal

UiK8SAppsInstallCreateAnnotationsErrorComponentAttr = Literal["annotations"]

UI_K8S_APPS_INSTALL_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_ui_k8s_apps_install_create_annotations_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateAnnotationsErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
