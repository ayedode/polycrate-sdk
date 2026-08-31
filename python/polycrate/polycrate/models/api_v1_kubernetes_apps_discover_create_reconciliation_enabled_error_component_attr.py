from typing import Literal

ApiV1KubernetesAppsDiscoverCreateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_kubernetes_apps_discover_create_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
