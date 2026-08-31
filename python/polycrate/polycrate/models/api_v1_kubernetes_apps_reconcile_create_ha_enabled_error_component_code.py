from typing import Literal

ApiV1KubernetesAppsReconcileCreateHaEnabledErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_HA_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateHaEnabledErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_apps_reconcile_create_ha_enabled_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateHaEnabledErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_HA_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_HA_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
