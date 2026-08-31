from typing import Literal

UiK8SAppsInstallCreateExcludedFromDowntimeUntilErrorComponentAttr = Literal["excluded_from_downtime_until"]

UI_K8S_APPS_INSTALL_CREATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateExcludedFromDowntimeUntilErrorComponentAttr
] = {
    "excluded_from_downtime_until",
}


def check_ui_k8s_apps_install_create_excluded_from_downtime_until_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateExcludedFromDowntimeUntilErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
