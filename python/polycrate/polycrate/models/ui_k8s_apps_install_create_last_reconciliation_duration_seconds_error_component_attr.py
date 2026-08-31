from typing import Literal

UiK8SAppsInstallCreateLastReconciliationDurationSecondsErrorComponentAttr = Literal[
    "last_reconciliation_duration_seconds"
]

UI_K8S_APPS_INSTALL_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateLastReconciliationDurationSecondsErrorComponentAttr
] = {
    "last_reconciliation_duration_seconds",
}


def check_ui_k8s_apps_install_create_last_reconciliation_duration_seconds_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateLastReconciliationDurationSecondsErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
