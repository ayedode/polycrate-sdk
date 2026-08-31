from typing import Literal

UiK8SAppsInstallCreateSloWindowDaysErrorComponentAttr = Literal["slo_window_days"]

UI_K8S_APPS_INSTALL_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateSloWindowDaysErrorComponentAttr
] = {
    "slo_window_days",
}


def check_ui_k8s_apps_install_create_slo_window_days_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateSloWindowDaysErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
