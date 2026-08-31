from typing import Literal

UiK8SAppsUninstallCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

UI_K8S_APPS_UNINSTALL_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_ui_k8s_apps_uninstall_create_sla_availability_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateSlaAvailabilityErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
