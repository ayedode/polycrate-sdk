from typing import Literal

UiK8SAppsUninstallCreateCriticalityErrorComponentAttr = Literal["criticality"]

UI_K8S_APPS_UNINSTALL_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_ui_k8s_apps_uninstall_create_criticality_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateCriticalityErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
