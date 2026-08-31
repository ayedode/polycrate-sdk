from typing import Literal

UiK8SAppsInstallCreateSourceErrorComponentAttr = Literal["source"]

UI_K8S_APPS_INSTALL_CREATE_SOURCE_ERROR_COMPONENT_ATTR_VALUES: set[UiK8SAppsInstallCreateSourceErrorComponentAttr] = {
    "source",
}


def check_ui_k8s_apps_install_create_source_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateSourceErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_SOURCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_SOURCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
