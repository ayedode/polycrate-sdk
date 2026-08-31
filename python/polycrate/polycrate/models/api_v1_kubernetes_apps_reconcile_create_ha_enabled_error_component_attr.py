from typing import Literal

ApiV1KubernetesAppsReconcileCreateHaEnabledErrorComponentAttr = Literal["ha_enabled"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_HA_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateHaEnabledErrorComponentAttr
] = {
    "ha_enabled",
}


def check_api_v1_kubernetes_apps_reconcile_create_ha_enabled_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateHaEnabledErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_HA_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_HA_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
