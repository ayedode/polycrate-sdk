from typing import Literal

UiK8SAppsUninstallCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

UI_K8S_APPS_UNINSTALL_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsUninstallCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_ui_k8s_apps_uninstall_create_reconciliation_enabled_error_component_code(
    value: str,
) -> UiK8SAppsUninstallCreateReconciliationEnabledErrorComponentCode:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
