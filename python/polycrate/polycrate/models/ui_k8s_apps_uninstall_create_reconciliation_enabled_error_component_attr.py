from typing import Literal

UiK8SAppsUninstallCreateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

UI_K8S_APPS_UNINSTALL_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_ui_k8s_apps_uninstall_create_reconciliation_enabled_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateReconciliationEnabledErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
