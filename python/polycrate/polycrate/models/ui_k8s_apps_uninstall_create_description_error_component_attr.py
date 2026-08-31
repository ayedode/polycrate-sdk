from typing import Literal

UiK8SAppsUninstallCreateDescriptionErrorComponentAttr = Literal["description"]

UI_K8S_APPS_UNINSTALL_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_ui_k8s_apps_uninstall_create_description_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateDescriptionErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
