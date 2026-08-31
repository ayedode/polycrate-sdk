from typing import Literal

UiK8SAppsInstallCreateSlaWindowDaysErrorComponentAttr = Literal["sla_window_days"]

UI_K8S_APPS_INSTALL_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateSlaWindowDaysErrorComponentAttr
] = {
    "sla_window_days",
}


def check_ui_k8s_apps_install_create_sla_window_days_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateSlaWindowDaysErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
