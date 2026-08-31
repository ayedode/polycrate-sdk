from typing import Literal

UiK8SAppsInstallCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

UI_K8S_APPS_INSTALL_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_ui_k8s_apps_install_create_target_availability_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateTargetAvailabilityErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
