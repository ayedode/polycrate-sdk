from typing import Literal

UiK8SAppsInstallCreateLastReconciliationDurationSecondsErrorComponentCode = Literal["invalid", "max_string_length"]

UI_K8S_APPS_INSTALL_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsInstallCreateLastReconciliationDurationSecondsErrorComponentCode
] = {
    "invalid",
    "max_string_length",
}


def check_ui_k8s_apps_install_create_last_reconciliation_duration_seconds_error_component_code(
    value: str,
) -> UiK8SAppsInstallCreateLastReconciliationDurationSecondsErrorComponentCode:
    if value in UI_K8S_APPS_INSTALL_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
