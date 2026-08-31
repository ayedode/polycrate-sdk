from typing import Literal

UiK8SAppsUninstallCreateByoaErrorComponentAttr = Literal["byoa"]

UI_K8S_APPS_UNINSTALL_CREATE_BYOA_ERROR_COMPONENT_ATTR_VALUES: set[UiK8SAppsUninstallCreateByoaErrorComponentAttr] = {
    "byoa",
}


def check_ui_k8s_apps_uninstall_create_byoa_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateByoaErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_BYOA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_BYOA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
