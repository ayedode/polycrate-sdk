from typing import Literal

ApiV1KubernetesAppsReconcileCreateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_kubernetes_apps_reconcile_create_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
