from typing import Literal

UiK8SAppsUninstallCreateActiveErrorComponentAttr = Literal["active"]

UI_K8S_APPS_UNINSTALL_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateActiveErrorComponentAttr
] = {
    "active",
}


def check_ui_k8s_apps_uninstall_create_active_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateActiveErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
