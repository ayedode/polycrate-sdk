from typing import Literal

ApiV1KubernetesAppsUpdateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsUpdateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_update_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsUpdateReconciliationEnabledErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
