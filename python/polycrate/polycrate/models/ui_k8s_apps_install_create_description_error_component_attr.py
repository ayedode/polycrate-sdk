from typing import Literal

UiK8SAppsInstallCreateDescriptionErrorComponentAttr = Literal["description"]

UI_K8S_APPS_INSTALL_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_ui_k8s_apps_install_create_description_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateDescriptionErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
