from typing import Literal

ApiV1KubernetesAppsReconcileCreateDiscoveryEnabledErrorComponentAttr = Literal["discovery_enabled"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateDiscoveryEnabledErrorComponentAttr
] = {
    "discovery_enabled",
}


def check_api_v1_kubernetes_apps_reconcile_create_discovery_enabled_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateDiscoveryEnabledErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
