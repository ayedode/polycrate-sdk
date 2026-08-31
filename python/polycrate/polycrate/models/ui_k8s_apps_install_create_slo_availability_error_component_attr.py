from typing import Literal

UiK8SAppsInstallCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

UI_K8S_APPS_INSTALL_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_ui_k8s_apps_install_create_slo_availability_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateSloAvailabilityErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
