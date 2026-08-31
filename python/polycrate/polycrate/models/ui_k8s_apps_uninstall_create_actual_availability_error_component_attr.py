from typing import Literal

UiK8SAppsUninstallCreateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

UI_K8S_APPS_UNINSTALL_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_ui_k8s_apps_uninstall_create_actual_availability_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateActualAvailabilityErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
