from typing import Literal

UiK8SAppsUninstallCreateUninstallationFailedErrorComponentAttr = Literal["uninstallation_failed"]

UI_K8S_APPS_UNINSTALL_CREATE_UNINSTALLATION_FAILED_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateUninstallationFailedErrorComponentAttr
] = {
    "uninstallation_failed",
}


def check_ui_k8s_apps_uninstall_create_uninstallation_failed_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateUninstallationFailedErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_UNINSTALLATION_FAILED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_UNINSTALLATION_FAILED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
