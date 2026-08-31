from typing import Literal

UiK8SAppsUninstallCreateSloWindowDaysErrorComponentAttr = Literal["slo_window_days"]

UI_K8S_APPS_UNINSTALL_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateSloWindowDaysErrorComponentAttr
] = {
    "slo_window_days",
}


def check_ui_k8s_apps_uninstall_create_slo_window_days_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateSloWindowDaysErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
