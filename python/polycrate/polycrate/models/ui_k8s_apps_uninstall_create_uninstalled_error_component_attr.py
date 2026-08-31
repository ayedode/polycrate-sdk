from typing import Literal

UiK8SAppsUninstallCreateUninstalledErrorComponentAttr = Literal["uninstalled"]

UI_K8S_APPS_UNINSTALL_CREATE_UNINSTALLED_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateUninstalledErrorComponentAttr
] = {
    "uninstalled",
}


def check_ui_k8s_apps_uninstall_create_uninstalled_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateUninstalledErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_UNINSTALLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_UNINSTALLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
