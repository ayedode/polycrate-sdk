from typing import Literal

UiK8SAppsUninstallCreateNameErrorComponentAttr = Literal["name"]

UI_K8S_APPS_UNINSTALL_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[UiK8SAppsUninstallCreateNameErrorComponentAttr] = {
    "name",
}


def check_ui_k8s_apps_uninstall_create_name_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateNameErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
